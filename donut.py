# SUMMARY OF WHAT'S HAPPENING
import math
import pygame

pygame.init()

# 2 colors
white = (255, 255, 255)  # donut
black = (0, 0, 0)  # background

# setting pygame window size
WIDTH = 1920
HEIGHT = 1080

# ----------------------------------------------------------------------------------------------------------------

# D O N U T _ S E T U P

x_start, y_start = 0, 0  # left top corner starting position

# space between chars
x_separator = 10
y_separator = 20

# rows, columns, and screen size
rows = HEIGHT // y_separator
columns = WIDTH // x_separator
screen_size = rows * columns

# D O N U T _ C R E A T I O N

# drawing donut in middle of the screen
x_offset = columns / 2
y_offset = rows / 2

# rotation animation
A, B = 0, 0

# creating donut white
theta_spacing = 10  # density of primary cirle
phi_spacing = 1  # donut density amonst primary circle 360°

# chars for illuminate index
chars = ".,-~:;=!*#$@"

# ---------------------------------------------------------------------------------------------------------------

# R E N D E R I N G

# screen for pygame window, size of screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))

# or if you choose to use fullscreen -- uncomment to use
# display_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN);

# caption and font
pygame.display.set_caption('Spinning Donut')
font = pygame.font.SysFont('Inter', 18, bold=True)


def text_display(letter, x_space, y_space):
    """
    This is a display function
    need parameters for characters and coordinates on screen
    """
    text = font.render(str(letter), True, white)
    # bleed text on pygame surface
    display_surface.blit(text, (x_start, y_start))


# ---------------------------------------------------------------------------------------------------------------

# R U N N I N G

# pygame runs in a while loop
run = True
while run:

    # start
    screen.fill(black)

    # spinning donut

    pygame.display.update()

    # close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run == False
