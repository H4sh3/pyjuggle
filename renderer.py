import pygame

def render_hand(screen,hand):
    pygame.draw.circle(screen, (0, 0, 255), (hand[0], hand[1]), 50)


def render_ball(screen,ball):
    pygame.draw.circle(screen, (0, 0, 255), (ball.pos[0], ball.pos[1]), 15)