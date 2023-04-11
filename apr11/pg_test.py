import pygame


# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Game constants
WIDTH = 360
HEIGHT = 480
FPS = 60

# Initialize
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hello")
clock = pygame.time.Clock()

# Init game loop

running = True
x = 100
y = 100
x_change = 0
y_change = 0

# Game loop
while running:
    # 1 Process input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -2
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = 2
                y_change = 0
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = -2
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = 2
                
    
    # 2 Update
    x += x_change
    y += y_change
    
    if not(0 < x < WIDTH - 10):
        x_change *= -1
        
    if not(0 < y < HEIGHT -10):
        y_change *= -1
    
    # 3 Draw
    screen.fill(BLACK)
    
    pygame.draw.rect(screen, RED, (x, y, 10, 10))
    
    
    # 4 clock tick
    clock.tick(FPS)
    
    # 5 flip screen
    pygame.display.flip()
    
pygame.quit()