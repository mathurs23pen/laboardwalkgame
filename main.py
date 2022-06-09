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
def scoreboard(score):
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
score = 0
scoreboard(score)
class questionclass: 
    def __init__(self, question, choiceone, choicetwo, choicethree, answer): 
        self.question = question 
        self.choiceone = choiceone
        self.choicetwo = choicetwo
        self.choicethree = choicethree
        self.answer = answer
questions = []
#STEAL
questions.append(questionclass(
   "Does Chad think Jason is the type of person to do drugs?",
   "Yes",
   "No",
   "A purple elephant",
   2))
questions.append(questionclass(
   "Which character from Wonder is Anthony most similar to?",
   "Auggie",
   "Summer",
   "Julian",
   3))
questions.append(questionclass(
   "What kind of a person is Chad before Malcolm \nfights Chad and shows him how good his life is?",
   "Energetic, like a radioactive dog.",
   "Tries everything and is \nnot afraid of failing.",
   "Does not try because he \nis afraid of failing.",
   3))
questions.append(questionclass(
   "Why is Manetti always so nice to Chad?",
   "Manetti is the good cop.",
   "He understands how Chad feels.",
   "He is Chad.",
   2))
#Conflict
questions.append(questionclass(
   "Which of the following characters does Gwen go out with?",
   "Anthony",
   "Jason",
   "A purple elephant",
   1))
questions.append(questionclass(
   "Why do you think Anthony decided to ask Gwen out? \nSelect the option that can be proven using evidence from the book.",
   "Anthony decided to ask \nGwen out because \nhe knew it would annoy Chad. \nHe may have also genuinely \nliked her, but if you consider \nhow different he is from Gwen, \nthat is probably not the case.",
   "Anthony decided to ask Gwen \nout because he needed \na partner in crime and \nthought she would be \neasy to control.",
   "Anthony decided to ask Gwen \nout because Chad told \nhim that they would \ngo well together. He \nknew that Chad was a \nnice person, so he listened.",
   1))
questions.append(questionclass(
   "How does Jason's sickness affect Chad? \nSelect the answer that is NOT correct.",
   "Positively, Chad is able to \npractice being a Bozo \nand feel like he's \nbeing helpful.",
   "Negatively, the fact that Chad \nfelt like he was losing \nhis best friend was \npart of the reason he \nwent to the couch.",
   "Negatively. Because of this, \nChad can't be a Bozo because \nhe wanted to do it with Jason.",
   3))
questions.append(questionclass(
   "How does Chad feel when Gwen tells him about the party? \nWhy does he feel this way?",
   "Angry because he thinks \nAnthony has corrupted \nher. He views her \nas Little Miss Perfect \nand feels that being \nwith Anthony \nwould ruin her.",
   "Angry because he feels like \nhe has been robbed of one \nof his possessions. \nHe took a risk when he \nasked her to be his girlfriend \nand then she ran off with \nthe man who killed his father.",
   "Guilty because he realizes \nthat he should've \nasked her out before so \nthat Anthony couldn't \nsteal her from him.",
   1))
#Theme
questions.append(questionclass(
   "Which theme is backed up by correct evidence?",
   "The real radioactive bunnies \nare the friends you \nmake along the way. This \nis proven by the \nnumber of times Chad \nasks for a purple \ngiraffe with horns.",
   "'Be yourself. Your real \nfriends will like you for \nyou.' This is backed \nup by the fact that Gwen \naccepts Chad when he \nreveals his true \nfeelings without holding \nanything back.",
   "'Make good choices.' This \nis proven by the fact that \nhe is sad after buying \na giraffe instead of \na bunny.",
   2))
questions.append(questionclass(
   "What is a theme of the book?",
   "You can't get rejected \nif you don't try, so don't \neven make an attempt \nat doing anything.",
   "Purple bunnies are radioactive, \nso you should stay away from them.",
   "You can't succeed if you don't try, \nso you have to make an attempt.",
   3))
questions.append(questionclass(
   "How does the title reflect the events in \nthe book? Select the INCORRECT answer.",
   "It shows how Chad has been \ndunked many times in \nhis actual life and \nthe ups and downs \nhe goes through",
   "He wants to be the \nBozo and be dunked",
   "He's never gonna give you up", 3))
questions.append(questionclass(
   "Which of these events reveal the most about Chad's character?", 
   "Chad deciding not to quit \nbeing a Ballzo even though he hates it.",
   "When rainbow elephant dies",
   "When Jason gets sick",
   1))
#Signpost
questions.append(questionclass(
   "Which of these is a valid signpost?",
   "All of chapter 7 is a \nMemory Moment because \nChad is remembering \nlast summer, when he met Gwen.",
   "All of chapter 7 is a \nContrasts and \nContradictions because \nit is unexpected for \nChad to be so obsessed with a girl",
   "All of chapter 7 is a tough \nquestion because Chad \nis asking himself why he \nhas fallen in love \nwith a girl.",
   1))
questions.append(questionclass(
   "Which of the following characters gives Chad advice? (Words of the Wiser)",
   "Corey",
   "Malcolm",
   "A purple elephant",
   2))
questions.append(questionclass(
   "Why does the narrator, Chad, keep bringing up the fact that \nhe wants to see Gwen before she comes back? (Again and again)",
   "Chad really wants to see Gwen \nagain because he wants to \nbecome friends with her",
   "Chad really wants to see Gwen \nagain because he wants \nto ask her out",
   "Chad really wants to see Gwen \nagain because he wants her \nto meet Anthony so \nthat they can become a thing",
   2))
questions.append(questionclass("Which of the following is an example of Contrasts and Contradictions.", "In chapter one, when Chad watches the Bozo.", "Malcolm bailing Chad out of jail.", "Malcolm giving up his job for Chad.", 2))
#Plot
questions.append(questionclass(
   "Who does Chad like (romantically, not platonically)?",
   "A purple elephant",
   "Yes",
   "Gwen",
   3))
questions.append(questionclass(
   "Why does Jason want to go to California?",
   "He wants to meet 69 \npurple elephants.",
   "He wants to play volleyball \nand meet cute college \ngirls at the Santa \nMonica pier.",
   "His parents like it there.",
   2))
questions.append(questionclass(
   "Why is Chad disappointed about his job in chapter 13?",
   "He thought he was going to \nbe a Bozo, but instead \nhe was the Bozo's ball \nboy. This is a very strenuous \nand taxing job.",
   "He thought he was going \nto be Barney but instead \nhe was Bart Simpson.",
   "He wanted to work with \nMalcolm but instead \nhe had to collect \nballs for him.",
   1))
questions.append(questionclass(
   "Why does Jason’s mom hate Chad and doesn't want him to be around Jason?",
   "She is (221, 199, 160), \nwhich is beige \n(the most boring of colors). \nThis has nothing to do with \nher skin color. \nShe is just boring.",
   "She thinks chad was the \nreason Jason got sick",
   "She thinks Chad is Barney.",
   2))
#Function to display questions
def questionfunc():
    global questionnum
    questionnum=0
    shuffle(questions)
    shape("square")
    resizemode("user")
    shapesize(9, 120)
    color("#2A0332")
    pu()
    goto(0, 290)
    pd()
    stamp()
    pu()
    goto(0, 280)
    pd()
    color("white")
    write(questions[questionnum].question, False, "center", ("Arial", 20, "normal"))
    pu()
    goto(-300, -180)
    pd()
    color("#2A0332")
    stamp()
    color("white")
    pu()
    goto(-300, -230)
    pd()
    write(questions[questionnum].choiceone, False, "center", ("Arial", 18, "normal"))
    pu()
    goto(0, -230)
    pd()
    write(questions[questionnum].choicetwo, False, "center", ("Arial", 18, "normal"))
    pu()
    goto(300, -230)
    pd()
    write(questions[questionnum].choicethree, False, "center", ("Arial", 18, "normal"))
    global userinput
    userinput=0
questionfunc()
score=0
def key1():
    userinput = 1
    if userinput==questions[0].answer:
        global score
        score+=100
        scoreboard(score)
        questionfunc()
    elif userinput == 0:
        scoreboard()
    else:
        score-=200
        scoreboard(score)
        questionfunc()
def key2():
    userinput = 2
    if userinput==questions[0].answer:
        global score
        score+=100
        scoreboard(score)
        questionfunc()
    elif userinput == 0:
        scoreboard()
    else:
        score-=200
        scoreboard(score)
        questionfunc()
def key3():
    userinput = 3
    if userinput==questions[0].answer:
        global score
        score+=100
        scoreboard(score)
        questionfunc()
    elif userinput == 0:
        scoreboard()
    else:
        score-=200
        scoreboard(score)
        questionfunc()
onkey(key1, "1")
onkey(key2, "2")
onkey(key3, "3")
listen()
