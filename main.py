# Simple pygame program

# Import and initialize the pygame library

from config import height,width
from juggle import Juggle
import renderer as Renderer

import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([width, height])

# Run until the user asks to quit

j = Juggle()


running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    j.step({})

    for ball in j.balls:
        Renderer.render_ball(screen,ball)

    Renderer.render_hand(screen,j.hand_left)
    Renderer.render_hand(screen,j.hand_right)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()