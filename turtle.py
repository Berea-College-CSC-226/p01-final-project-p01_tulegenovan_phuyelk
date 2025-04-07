import pygame
import random
import time

pygame.init()

screen_width = 700
screen_height = 700

screen = pygame.display.set_mode((screen_width, screen_height))

turtle_image = pygame.image.load('image/turtle.png').convert_alpha()
turtle_image.set_colorkey((255, 255, 255), pygame.RLEACCEL)




class TurtleObject:

    def __init__(self):
        self.size = 50
        self.image = turtle_image
        self.x = random.randint(0, screen_width)
        self.y = random.randint(0, screen_height)
        self.visible = True

        self.last_move_time = time.time() # save current time
        self.move_interval = 1

    def move(self):
        self.x = random.randint(0, screen_width - self.size)
        self.y = random.randint(0, screen_height - self.size)
        self.last_move_time = time.time()
        self.visible = True

    def draw(self, screen):
        # Blit the image to the Pygame screen
        if self.visible:
            screen.blit(self.image, (self.x, self.y))

    def is_clicked(self, mouse_pos):
        if not self.visible:
            return False
        px, py = mouse_pos
        return self.x <= px <= self.x + self.size and self.y <= py <= self.y + self.size

    def update(self):
         if time.time()- self.last_move_time > self.move_interval:
             self.move()


game_turtle = TurtleObject()
score = 0
start_time = time.time
duration = 20
# game loop
running = True

screen.fill((0, 0, 0))  # Clear the screen with black

    # Draw the game turtle
game_turtle.draw(screen)

    # Update the screen
pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()


# Quit pygame
pygame.quit()













