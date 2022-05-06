from turtle import *
import pygame
WIDTH, HEIGHT = 1025, 775
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
ORANGE = (237, 89, 14)
pygame.display.set_mode((500, 500))
pygame.image.load("resources/whacamoleimg.png")
pygame.draw.circle(WIN, (ORANGE), (83, 30), 8)
