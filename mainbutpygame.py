from turtle import *
import pygame
pygame.init()
x=1
size=(700,500)
screen = pygame.display.set_mode((500, 500))
while x<54:
    circle(x, None, None)
    x=x+1