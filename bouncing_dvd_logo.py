import pygame
from random import randint

pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode([800, 600])
white = [255, 255, 255]
screen.fill(white)

pygame.display.set_caption('DVD Bouncing Logo!')

logo_image = pygame.image.load("dvd_logo.png")
logo_image = pygame.transform.scale(logo_image, (104, 104))

class Logo:
        def __init__(self, speed):
                self.x_speed = speed
                self.y_speed = speed
                self.x = randint(0, screen.get_height() - logo_image.get_height())
                self.y = randint(0, screen.get_width() - logo_image.get_width())

        def move(self):
                print(self.x)
                print(self.y)
                self.x = self.x + self.x_speed
                self.y = self.y + self.y_speed


logo = Logo(3)


def is_on_edge():
        if logo_image.get_width:
                pass


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
