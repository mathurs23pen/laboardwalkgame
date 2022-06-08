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
questions.append(questionclass("What kind of a person is Chad before Malcolm fights Chad and shows him how good his life is?", "Energetic, like a radioactive dog.", "Tries everything and is not afraid of failing.", "Does not try because he is afraid of failing.", 3))
questions.append(questionclass("Why is Manetti always so nice to Chad?", "Manetti is the good cop.", "He understands how Chad feels.", "He is Chad.", 3))
#Conflict
questions.append(questionclass("Which of the following characters does Gwen go out with?", "Anthony", "Jason", "A purple elephant", 2))
questions.append(questionclass("Why do you think Anthony decided to ask Gwen out? Select the option that can be proven using evidence from the book.", "Anthony decided to ask Gwen out because he knew it would annoy Chad. He may have also genuinely liked her, but if you consider how different he is from Gwen, that is probably not the case.", "Anthony decided to ask Gwen out because he needed a partner in crime and thought she would be easy to control.", "Anthony decided to ask Gwen out because Chad told him that they would go well together. He knew that Chad was a nice person, so he listened.", 1))
questions.append(questionclass("How does Jason's sickness affect Chad? Select the answer that is not correct.", "Positively, Chad is able to practice being a Bozo and feel like he's helping Jason.", "Negatively, the fact that Chad felt like he was losing his best friend was part of the reason he went to the couch.", "Negatively. Because of this, Chad can't be a Bozo because he wanted to do it with Jason.", 3))
questions.append(questionclass("How does Chad feel when Gwen tells him about the party? Why does he feel this way?", "Angry because he thinks Anthony has corrupted her. He views her as Little Miss Perfect and feels that being with Anthony would ruin her.", "Angry because he feels like he has been robbed of one of his possessions. He took a risk when he asked her to be his girlfriend and then she ran off with his nemesis.", "Guilty because he realizes that he should've asked her out before so that Anthony couldn't steal her from him.", 1))
#Theme
questions.append(questionclass("Which theme is backed up by correct evidence?", "The real radioactive bunnies are the friends you make along the way. This is proven by the number of times Chad asks for a purple giraffe with horns.", "'Be yourself. Your real friends will like you for you.' This is backed up by the fact that Gwen accepts Chad when he reveals his true feelings without holding anything back.", "'Make good choices.' This is proven by the fact that he is sad after buying a giraffe instead of a bunny.", 2))
questions.append(questionclass("What is a theme of the book?", "You can't get rejected if you don't try, so don't even make an attempt at doing anything.", "Purple bunnies are radioactive, so you should stay away from them." "You can't succeed if you don't try, so you have to make an attempt.", 3))
questions.append(questionclass("How is the title of the book similar to what is in the book?", "It shows how Chad has been dunked many times in his actual life and the downs he goes through", "he wants to be the Bozo and be dunked", "he’s never gonna give you up", 1))
questions.append(questionclass("Which of these events reveal the most about Chad’s character?",  "Chad deciding not to quit being a Ballzo even though he hates it.", "When rainbow elephant dies", "When Jason gets sick", 1))
#Signpost
questions.append(questionclass("Which of these is a valid signpost?", "All of chapter 7 is a Memory Moment because Chad is remembering last summer, when he met Gwen.", "All of chapter 7 is a Contrasts and Contradictions because it is unexpected for Chad to be so obsessed with a girl", "All of chapter 7 is a tough question because Chad is asking himself why he has fallen in love with a girl.", 1))
questions.append(questionclass("Which of the following characters gives Chad advice? (Words of the Wiser)", "Corey", "Malcolm", "A purple elephant"))
#questions.append(questionclass())
#questions.append(questionclass())
#Plot
questions.append(questionclass("Who does Chad like (romantically, not platonically)?", "A purple elephant", "Yes", "Gwen", 3))
questions.append(questionclass("Why does Jason want to go to California?", "He wants to meet 69 purple elephant.", "He wants to play volleyball and meet cute college girls at the Santa Monica pier.", "His parents like it there.", 2))
questions.append(questionclass("Why is Chad disappointed about his job in chapter 13?", "He thought he was going to be a Bozo, but instead he was the Bozo's ball boy. This is a very strenuous and taxing job.", "He thought he was going to be Barney but instead he was Bart Simpson.", "He wanted to work with Malcolm but instead he had to collect balls for him.", 1))
questions.append(questionclass("Why does Jason’s mom hate Chad and doesn't want him to be around Jason?", "She is (221, 199, 160), which is beige (the most boring of colors).", "She thinks chad was the reason Jason got sick", "She thinks Chad is Barney.", 2))
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
