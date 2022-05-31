from turtle import *
from random import *
import keyboard
setup(1000,752)
hideturtle()
speed(0)
bgpic("resources/bgpic.png")
screen = Screen()
image = "resources/spaceship1.gif"
screen.addshape(image)
shape(image)
x=-300
while x<600:
    goto(x, 0)
    stamp()
    x=x+300
questions = [
    #STEAL
    "Does Chad think Jason is the type of person to do drugs?",
    #Conflict
    "Which of the following characters does Gwen go out with?",
    "Why do you think Anthony decided to ask Gwen out? Select the best option"
    #Theme
    #Signpost
    #Plot
    "Who does Chad like (romantically, not platonically)?"
    ]
def questionfunc(questionnum):
    shuffle(questions)
    write(questions[questionnum], False, "center", ("Arial", 20, "normal"))
    delay(9999)
    undo()
goto(0, 200)