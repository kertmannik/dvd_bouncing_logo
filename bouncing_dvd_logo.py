import pygame
from random import randint

pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()
fps = 30

screen = pygame.display.set_mode([800, 600])
white = [255, 255, 255]
screen_color = white
screen.fill(screen_color)
screen_width = screen.get_width()
screen_height = screen.get_height()

pygame.display.set_caption('Bouncing DVD Logo!')

logo_image = pygame.image.load("dvd_logo.png")
logo_image = pygame.transform.scale(logo_image, (158, 70))

logo_width = logo_image.get_width()
logo_height = logo_image.get_height()

class Logo:
        def __init__(self, speed):
                self.x_speed = speed
                self.y_speed = speed
                self.x = randint(0, screen_height - logo_height)
                self.y = randint(0, screen_width - logo_width)

        def move(self):
                self.x = self.x + self.x_speed
                self.y = self.y + self.y_speed

        def is_on_edge(self):
            if self.x + logo_width >= screen_width:
                self.x_speed = -self.x_speed
                self.x = screen_width - logo_width
                random_background_color()
            elif self.x <= 0:
                self.x_speed = -self.x_speed
                self.x = 0
                random_background_color()

            if self.y + logo_height >= screen_height:
                self.y_speed = -self.y_speed
                self.y = screen_height - logo_height
                random_background_color()
            elif self.y <= 0:
                self.y_speed = -self.y_speed
                self.y = 0
                random_background_color()


logo = Logo(3)


def random_background_color():
    global screen_color
    r = randint(100, 256)
    g = randint(100, 256)
    b = randint(100, 256)
    screen_color = (r, g, b)


def refresh_screen():
        screen.fill(screen_color)
        screen.blit(logo_image, (logo.x, logo.y))
        pygame.display.flip()
        clock.tick(fps)


while True:
    for event in pygame.event.get():
        pass
    logo.is_on_edge()
    logo.move()
    refresh_screen()
