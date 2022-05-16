from turtle import *
setup(1000,752)
hideturtle()
speed(0)
bgpic("resources/bgpic.png")
screen = Screen()
image = "resources/spaceship1.gif"
screen.addshape(image)
shape(image)
x=-300
while x<900:
    goto(x, 0)
    stamp()
    x=x+300
