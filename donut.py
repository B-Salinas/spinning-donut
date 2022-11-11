# later: summary of what's happening / what's about to happen in the code

# Preparing Pygame window
import pygame

pygame.init()

#  -- 2 colors
# donut
white = (255, 255, 255)
# background
black = (0, 0, 0)

# -- setting pygame window size
WIDTH = 1920
HEIGHT = 1080

# -- screen for pygame window, size of screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))

# or if you choose to use fullscreen -- uncomment to use
# display_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN);

pygame.display.set_caption('Spinning Donut')
font = pygame.font.SysFont('Inter', 18, bold=True)

# -- pygame is run in a while loop
run = True
while run:

    screen.fill(black)

    # spinning donut code goes here

    pygame.display.update()

    # -- close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run == False
