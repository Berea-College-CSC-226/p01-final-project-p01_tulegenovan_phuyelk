import pygame
import random
import time

pygame.init()

screen_width = 700
screen_height = 700

screen = pygame.display.set_mode((screen_width, screen_height))

turtle_image = pygame.image.load('image/turtle.png').convert_alpha()
turtle_image = pygame.transform.scale(turtle_image, (100, 100))
turtle_image.set_colorkey((255, 255, 255), pygame.RLEACCEL)


class TurtleObject:

    def __init__(self):
        self.size = 100
        self.image = turtle_image
        self.x = 0
        self.y = 0
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
start_time = time.time()
duration = 20

def game_timer(start_time, duration = 20):
    """Check if the timer has expired."""
    current_time = time.time()
    elapsed = current_time - start_time
    return elapsed >= duration


# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if game_turtle.is_clicked(mouse_pos):
                score+=1
                game_turtle.move()

    game_turtle.update()
    screen.fill((0, 0, 0))  # Clear the screen with black
    game_turtle.draw(screen)

    if game_timer(start_time, duration):
        print("Time's up")
        running = False

    pygame.display.flip()



# Quit pygame
pygame.quit()













