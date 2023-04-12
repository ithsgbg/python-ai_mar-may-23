import random
from collections import deque

import numpy as np
import torch
from game import BLOCK_SIZE, Direction, Point, SnakeGame
from model import LinearQNet, QTrainer
from plot import plot

# Define constants
MAX_MEMORY = 100_000  # Maximum number of previous experiences we are storing
BATCH_SIZE = 1000  # Number of experiences we use for training per batch

LEARNING_RATE = 0.001  # How fast the neural network learns
EPSILON_CONSTANT = (
    80  # How many iterations we want to take before we reach the minimum epsilon
)

INPUT_SIZE = 11  # Number of inputs to the neural network
HIDDEN_SIZE = 256  # Number of neurons in the hidden layer
OUTPUT_SIZE = 3  # Number of outputs from the neural network


class Agent:
    def __init__(self):
        self.n_games = 0  # Number of games played
        self.epsilon = 0  # Exploration rate
        self.gamma = 0.9  # Discount rate, must be between 0 and 1
        self.memory = deque(maxlen=MAX_MEMORY)  # Long term memory

        self.model = LinearQNet(INPUT_SIZE, HIDDEN_SIZE, OUTPUT_SIZE)
        self.trainer = QTrainer(self.model, lr=LEARNING_RATE, gamma=self.gamma)
        self.last_10_scores = [0] * 10

    def get_state(self, game):
        head = game.head

        danger_state = {
            "point_l": Point(head.x - BLOCK_SIZE, head.y),
            "point_r": Point(head.x + BLOCK_SIZE, head.y),
            "point_u": Point(head.x, head.y - BLOCK_SIZE),
            "point_d": Point(head.x, head.y + BLOCK_SIZE),
            "dir_l": game.direction == Direction.LEFT,
            "dir_r": game.direction == Direction.RIGHT,
            "dir_u": game.direction == Direction.UP,
            "dir_d": game.direction == Direction.DOWN,
        }

        state = [
            # Danger Path
            self._get_danger(danger_state, game, "straight"),
            self._get_danger(danger_state, game, "right"),
            self._get_danger(danger_state, game, "left"),
            # Current Direction
            danger_state["dir_l"],
            danger_state["dir_r"],
            danger_state["dir_u"],
            danger_state["dir_d"],
            # Food state
            game.food.x < head.x,  # Food is to the left
            game.food.x > head.x,  # Food is to the right
            game.food.y < head.y,  # Food is up
            game.food.y > head.y,  # Food is down
        ]

        return np.array(state, dtype=int)

    def _get_danger(self, danger_state, game, heading):
        if heading == "straight":
            return (
                (danger_state["dir_r"] and game._is_collision(danger_state["point_r"]))
                or (
                    danger_state["dir_l"]
                    and game._is_collision(danger_state["point_l"])
                )
                or (
                    danger_state["dir_u"]
                    and game._is_collision(danger_state["point_u"])
                )
                or (
                    danger_state["dir_d"]
                    and game._is_collision(danger_state["point_d"])
                )
            )
        elif heading == "right":
            return (
                (danger_state["dir_r"] and game._is_collision(danger_state["point_d"]))
                or (
                    danger_state["dir_l"]
                    and game._is_collision(danger_state["point_u"])
                )
                or (
                    danger_state["dir_u"]
                    and game._is_collision(danger_state["point_r"])
                )
                or (
                    danger_state["dir_d"]
                    and game._is_collision(danger_state["point_l"])
                )
            )
        else:  # Heading left
            return (
                (danger_state["dir_r"] and game._is_collision(danger_state["point_u"]))
                or (
                    danger_state["dir_l"]
                    and game._is_collision(danger_state["point_d"])
                )
                or (
                    danger_state["dir_u"]
                    and game._is_collision(danger_state["point_l"])
                )
                or (
                    danger_state["dir_d"]
                    and game._is_collision(danger_state["point_r"])
                )
            )

    def get_action(self, state):
        self.epsilon = EPSILON_CONSTANT - self.n_games

        final_action = [0, 0, 0]

        if random.randint(0, 200) < self.epsilon:
            move_idx = random.randint(0, 2)
        else:
            new_state = torch.tensor(state, dtype=torch.float)
            prediction = self.model(new_state)  # Calls the models forward method
            move_idx = torch.argmax(prediction).item()
        final_action[move_idx] = 1
        return final_action

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def train_long_memory(self):
        if len(self.memory) > BATCH_SIZE:
            step_sample = random.sample(self.memory, BATCH_SIZE)
        else:
            step_sample = self.memory

        states, actions, rewards, next_states, dones = zip(*step_sample)
        self.trainer.train_step(states, actions, rewards, next_states, dones)

    def train_short_memory(self, state, action, reward, next_state, done):
        self.trainer.train_step(state, action, reward, next_state, done)


def train():
    plot_score = []
    plot_mean = []
    plot_last_10 = []

    total_score = 0
    record_score = 0

    agent = Agent()
    game = SnakeGame(speed=120)

    # Training loop
    while True:
        # Get current state
        current_state = agent.get_state(game)

        # Get action
        action = agent.get_action(current_state)

        # Perform action
        done, reward, score = game.play_step_ai(action)
        done = not done

        # Get new state
        new_state = agent.get_state(game)

        # Train short memory
        agent.train_short_memory(current_state, action, reward, new_state, done)

        # Remember
        agent.remember(current_state, action, reward, new_state, done)

        if done:  # Game over, AI is dead
            # Reset game
            game.reset()
            agent.n_games += 1

            # Train long memory
            agent.train_long_memory()

            # Check if we have a new record
            if score > record_score:
                record_score = score
                agent.model.save()

            print(
                f"Game: {agent.n_games}\nScore: {score}\nRecord Score: {record_score}\n********************\n"
            )

            # Plot results
            agent.last_10_scores.append(score)
            agent.last_10_scores.pop(0)
            total_score += score

            mean_score = total_score / agent.n_games
            last_10_mean = sum(agent.last_10_scores) / 10

            plot_last_10.append(last_10_mean)
            plot_mean.append(mean_score)
            plot_score.append(score)

            plot(plot_score, plot_mean, plot_last_10)
