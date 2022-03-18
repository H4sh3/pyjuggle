import pygame

def render_hand(screen,hand):
    pygame.draw.circle(screen, (0, 0, 255), (hand.x, hand.y), 50)


def render_ball(screen,ball):
    pygame.draw.circle(screen, (0, 0, 255), (ball.pos.x, ball.pos.y), 15)