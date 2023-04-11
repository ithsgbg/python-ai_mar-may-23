from enum import Enum
import pygame
import random
import numpy as np


# Game Constants
BLOCK_SIZE = 20
SPEED = 20
COUNTDOWN = 3

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
GREEN1 = (0, 255, 0)
GREEN2 = (100, 255, 0)
RED = (255, 0, 0)


class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    

class SnakeGame:
    def __init__(self, width=640, height=480, speed=SPEED):
        self.width = width
        self.height = height
        self.speed = speed
        
        pygame.init()
        self.font = pygame.font.SysFont('arial', 25)
        
        # Init display
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()
        
        # Game variables
        self.head = None
        self.body = None
        self.direction = None
        self.score = 0
        self.food = None
        self.frame_iteration = 0
        self.iterations_since_reward = 0
        self.reset()

    def reset(self):
        self.direction = Direction.RIGHT
        self.head = Point(self.width / 2, self.height / 2)
        self.body = [
            self.head,
            Point(self.head.x - BLOCK_SIZE, self.head.y),
            Point(self.head.x - (2 * BLOCK_SIZE), self.head.y)
        ]

        self.score = 0
        self.frame_iteration = 0
        self.iterations_since_reward = 0
        self._place_food()
        
    def _place_food(self):
        x = random.randint(0, (self.width - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (self.height - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in self.body:
            self._place_food()

    
    def _move(self):
        new_head = self.body.pop()
        if self.direction == Direction.RIGHT:
            new_head.x = self.head.x + BLOCK_SIZE
            new_head.y = self.head.y
        if self.direction == Direction.LEFT:
            new_head.x = self.head.x - BLOCK_SIZE
            new_head.y = self.head.y
        if self.direction == Direction.UP:
            new_head.x = self.head.x
            new_head.y = self.head.y - BLOCK_SIZE
        if self.direction == Direction.DOWN:
            new_head.x = self.head.x 
            new_head.y = self.head.y + BLOCK_SIZE
            
        self.body.insert(0, new_head)
        self.head = new_head

    def _extend_snake(self):
        new_tail = Point(0, 0)
        if self.direction == Direction.RIGHT:
            new_tail.x = self.body[-1].x - BLOCK_SIZE
            new_tail.y = self.body[-1].y
        if self.direction == Direction.LEFT:
            new_tail.x = self.body[-1].x + BLOCK_SIZE
            new_tail.y = self.body[-1].y
        if self.direction == Direction.UP:
            new_tail.x = self.body[-1].x 
            new_tail.y = self.body[-1].y + BLOCK_SIZE
        if self.direction == Direction.DOWN:
            new_tail.x = self.body[-1].x 
            new_tail.y = self.body[-1].y - BLOCK_SIZE
            
        self.body.append(new_tail)
    
    def _is_collision(self, point=None):
        if not point:
            point = self.head
            
        # Check if snake head hits itself
        if point in self.body[1:]:
            return True
        
        # Hit wall
        return point.x > self.width - BLOCK_SIZE or \
            point.x < 0 or \
            point.y > self.height - BLOCK_SIZE or \
            point.y < 0

    def _update_ui(self):
        self.screen.fill(BLACK)
        
        # Draw head
        pygame.draw.rect(self.screen, GREEN1, pygame.Rect(self.head.x, self.head.y, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(self.screen, GREEN2, pygame.Rect(self.head.x + 4, self.head.y + 4, BLOCK_SIZE - 8, BLOCK_SIZE -8))
        
        # Draw body
        for body_part in self.body[1:]:
            pygame.draw.rect(self.screen, BLUE1, pygame.Rect(body_part.x, body_part.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.screen, BLUE2, pygame.Rect(body_part.x + 4, body_part.y + 4, BLOCK_SIZE - 8, BLOCK_SIZE -8))
            
        # Draw fruit
        pygame.draw.rect(self.screen, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))
        
        # Draw score
        text = self.font.render(f'Score: {self.score}', True, WHITE)
        self.screen.blit(text, (0, 0))
        
        pygame.display.flip()
        
    def play_step_human(self):
        # 1. Collect user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.direction = Direction.LEFT
                if event.key == pygame.K_RIGHT:
                    self.direction = Direction.RIGHT
                if event.key == pygame.K_UP:
                    self.direction = Direction.UP
                if event.key == pygame.K_DOWN:
                    self.direction = Direction.DOWN
                    
        # 2. Move
        self._move()
        
        # 3. Check if game is over
        if self._is_collision():
            return False
        
        # 4. Check if food is reached
        if self.head == self.food:
            self.score += 1
            self._place_food()
            self._extend_snake()
        
        # 5. Update UI and clock
        self._update_ui()
        self.clock.tick(self.speed)
        
        # 6. Return game state
        return True
    
    def play_step_ai(self, action):
        self.iterations_since_reward += 1
        
        # Collect user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        # Convert ai action to new direction
        
        # Action is
        # [straight, right, left]
        # [1, 0, 0] -> Keep on going straight
        # [0, 1, 0] -> Turn right
        # [0, 0, 1] -> Turn left
        
        clockwise_dir = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]
        dir_idx = clockwise_dir.index(self.direction)
    
        if np.array_equal(action, [0, 1, 0]):  # Turn right
            dir_idx = (dir_idx + 1) % len(clockwise_dir)
        if np.array_equal(action, [0, 0, 1]):  # Turn left
            dir_idx = (dir_idx - 1) % len(clockwise_dir)

        self.direction = clockwise_dir[dir_idx]
    
        # 2. Move
        self._move()
    
        # 3. Check collision
        if self._is_collision():
            return False, -10, self.score
        elif self.iterations_since_reward > 100 * len(self.body):  # Snake is stuck
            return False, -5, self.score
        
        # 4. Check if food is reached
        if self.head == self.food:
            self.score += 1
            self._place_food()
            self._extend_snake()
            reward = 10
        else:
            reward = -0.1
    
        # 5. Update UI and clock
        self._update_ui()
        self.clock.tick(self.speed)
        
        # 6. Return game state
        return True, reward, self.score

    
    def countdown(self, countdown_time=COUNTDOWN):
        countdown_font = pygame.font.SysFont('arial', 50)
        for i in range(countdown_time, 0, -1):
            self._update_ui()
            
            # Process events to prevent freezing
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
            countdown_text = countdown_font.render(str(i), True, WHITE)
            self.screen.blit(countdown_text, (self.width // 2 - BLOCK_SIZE, self.height // 2 - BLOCK_SIZE))
            
            pygame.display.flip()
            
            pygame.time.wait(1000)
            
    @staticmethod
    def human_play():
        game = SnakeGame()
        game.countdown()
        # Game Loop
        running = True
        while running:
            running = game.play_step_human()
        print('Final score:', game.score)