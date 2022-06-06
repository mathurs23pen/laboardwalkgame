from turtle import *
from random import *
from playsound import playsound
from threading import Thread
t = Thread(target=playsound, args=["resources/Nu_Disco_-_Televisor_-_Neon_Mons_(getmp3.pro).mp3"])
t.start()
setup(1000,752)
hideturtle()
speed(0)
bgpic("resources/bgpic.png")
screen = Screen()
image = "resources/spaceship1.gif"
score = 0
def scoreboard():
    shape("square")
    resizemode("user")
    shapesize(4, 10)
    color("black")
    pu()
    goto(0, -300)
    pd()
    stamp()
    color("white")
    write(score, False, "center", ("arial", 20, "normal"))
screen.addshape(image)
shape(image)
x=-300
while x<600:
    pu()
    goto(x, 0)
    pd()
    stamp()
    x=x+300
scoreboard()
class questionclass: 
    def __init__(self, question, choiceone, choicetwo, choicethree, answer): 
        self.question = question 
        self.choiceone = choiceone
        self.choicetwo = choicetwo
        self.choicethree = choicethree
        self.answer = answer
questions = []
#STEAL
questions.append(questionclass("Does Chad think Jason is the type of person to do drugs?", "Yes", "No", "A purple elephant", 2))
questions.append(questionclass("Which character from Wonder is Anthony most similar to?", "Auggie", "Summer", "Julian", 3))
questions.append(questionclass("Why would officer Costas always blame Chad for doing something he has not done?", "He hates Chad personally", "He thinks he is just like his dad (bad and always getting into trouble)", "he sees the worst in people without looking for actual evidence also known as “McCarthyism”", 3))
def questionfunc(questionnum):
    shuffle(questions)
    shape("square")
    resizemode("user")
    shapesize(7, 100)
    color("#2A0332")
    pu()
    goto(0, 280)
    pd()
    stamp()
    color("white")
    write(questions[questionnum].question, False, "center", ("Arial", 20, "normal"))
pu()
goto(0, 200)
pd()
screen.onkey(questionfunc(0), "space")
screen.listen()