import pygame
import random
import time
# Initialize pygame
pygame.init()
# Screen setup
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Turtle Click Game")
# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)
# Fonts
font = pygame.font.SysFont(None, 36)
# Turtle class
class Turtle:
    def __init__(self):
        self.size = 50
        self.visible = True
        self.last_move_time = time.time()
        self.move_interval = 1  # seconds before turtle moves
        self.move()
    def move(self):
        self.x = random.randint(0, WIDTH - self.size)
        self.y = random.randint(0, HEIGHT - self.size)
        self.last_move_time = time.time()
        self.visible = True
    def draw(self):
        if self.visible:
            pygame.draw.rect(screen, GREEN, (self.x, self.y, self.size, self.size))
    def is_clicked(self, pos):
        if not self.visible:
            return False
        px, py = pos
        return self.x <= px <= self.x + self.size and self.y <= py <= self.y + self.size
    def update(self):
        if time.time() - self.last_move_time > self.move_interval:
            self.move()
# Game variables
turtle = Turtle()
score = 0
start_time = time.time()
game_duration = 20
running = True
# Game loop
while running:
    screen.fill(WHITE)
    current_time = time.time()
    time_left = max(0, int(game_duration - (current_time - start_time)))
    # Update turtle appearance
    turtle.update()