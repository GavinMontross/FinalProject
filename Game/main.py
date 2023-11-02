import pygame
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Platformer Game")

fps = 60
clock = pygame.time.Clock()

#put this in while run loop
clock.tick(fps)

