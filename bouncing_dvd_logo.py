import pygame
from random import randint

pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode([800, 600])
white = [255, 255, 255]
screen.fill(white)
screen_width = screen.get_width()
screen_height = screen.get_height()

pygame.display.set_caption('DVD Bouncing Logo!')

logo_image = pygame.image.load("dvd_logo.png")
logo_image = pygame.transform.scale(logo_image, (104, 104))

logo_width = logo_image.get_width()
logo_height = logo_image.get_height()

class Logo:
        def __init__(self, speed):
                self.x_speed = speed
                self.y_speed = speed
                self.x = randint(0, screen_height -logo_height)
                self.y = randint(0, screen_width - logo_width)

        def move(self):
                print(self.x)
                print(self.y)
                self.x = self.x + self.x_speed
                self.y = self.y + self.y_speed


logo = Logo(3)


def is_on_edge():
        if logo.x + logo_width >= screen_width:
                logo.x_speed = -logo.x_speed
                logo.x = screen_width - logo_width
        elif logo.x <= 0:
                logo.x_speed = -logo.x_speed
                logo.x = 0

        if logo.y + logo_height >= screen_height:
                logo.y_speed = -logo.y_speed
                logo.y = screen_height - logo_height
        elif logo.y <= 0:
                logo.y_speed = -logo.y_speed
                logo.y = 0


def move_logo():
        logo.move()


def refresh_screen():
        screen.fill(white)
        screen.blit(logo_image, (logo.x, logo.y))
        pygame.display.flip()
        clock.tick(30)


while True:
        is_on_edge()
        move_logo()
        refresh_screen()
