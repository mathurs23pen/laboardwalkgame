from turtle import *
from random import *
from pynput.mouse import listener
from playsound import playsound
from threading import Thread
t = Thread(target=playsound, args=["resources/Nu_Disco_-_Televisor_-_Neon_Mons_(getmp3.pro).mp3"])
t.start()
setup(1000,752)
with Listener() as listener:
    listener.join()
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
#Actually displaying stuff on the screen
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
questions.append(questionclass("Why is Manetti always so nice to Chad?", "Manetti is the good cop.", "He understands how Chad feels.", "He is Chad.", 3))
#Conflict
questions.append(questionclass("Which of the following characters does Gwen go out with?", "Anthony", "Jason", "A purple elephant", 2))
questions.append(questionclass("Why do you think Anthony decided to ask Gwen out? Select the option that can be proven using evidence from the book.", "Anthony decided to ask Gwen out because he knew it would annoy Chad. He may have also genuinely liked her, but if you consider how different he is from Gwen, that is probably not the case.", "Anthony decided to ask Gwen out because he needed a partner in crime and thought she would be easy to control.", "Anthony decided to ask Gwen out because Chad told him that they would go well together. He knew that Chad was a nice person, so he listened.", 1))
questions.append(questionclass("How does Jason's sickness affect Chad? Select the answer that is not correct.", "Positively, Chad is able to practice being a Bozo and feel like he's helping Jason.", "Negatively, the fact that Chad felt like he was losing his best friend was part of the reason he went to the couch.", "Negatively. Because of this, Chad can't be a Bozo because he wanted to do it with Jason.", 3))
questions.append(questionclass("How does Chad feel when Gwen tells him about the party? Why does he feel this way?", "Angry because he thinks Anthony has corrupted her. He views her as Little Miss Perfect and feels that being with Anthony would ruin her.", "Angry because he feels like he has been robbed of one of his possessions. He took a risk when he asked her to be his girlfriend and then she ran off with his nemesis.", "Guilty because he realizes that he should've asked her out before so that Anthony couldn't steal her from him.", 1))
#Theme
#questions.append(questionclass())
#questions.append(questionclass())
#questions.append(questionclass())
#questions.append(questionclass())
#Signpost
#questions.append(questionclass())
#questions.append(questionclass())
#questions.append(questionclass())
#questions.append(questionclass())
#Plot
questions.append(questionclass("Who does Chad like (romantically, not platonically)?", ))
#questions.append(questionclass())
#questions.append(questionclass())
#questions.append(questionclass())
#Function to display questions
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
    goto(-300, -150)
    pd()
    color("#2A0332")
    stamp()
    color("white")
    write(questions[questionnum].choiceone, False, "center", ("Arial", 18, "normal"))
    pu()
    goto(0, -150)
    pd()
    write(questions[questionnum].choicetwo, False, "center", ("Arial", 18, "normal"))
    pu()
    goto(300, -150)
    pd()
    write(questions[questionnum].choicethree, False, "center", ("Arial", 18, "normal"))
def on_click(x, y, button, pressed):
    questionfunc(0)
