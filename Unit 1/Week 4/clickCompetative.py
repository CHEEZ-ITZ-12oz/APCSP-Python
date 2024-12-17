import turtle as trtl
import random
#setup ...............
name = input("Enter Name: ") # this is here to ask the user before making a screen
alonzo = "assets/alonzo.gif"
wn = trtl.Screen()
wn.addshape(alonzo)
spot = trtl.Turtle(shape="circle")
pen = trtl.Turtle()
pentime = trtl.Turtle()
start = trtl.Turtle(shape="circle")
trscore = trtl.Turtle()
clickCount = 0
timer = 0
highScores = []
# functions ...................
# functions - printing ...................
def printScores():
    ycor = 250
    for line in highScores:
        trscore.goto(-300,ycor)
        trscore.write(f"{line[0]}:  {line[1]} - Score: {line[2]}", font=("Comic Sans MS", 15, "normal"))
        ycor -= 30
def updateDisplay(drpen):
    drpen.clear()
    if drpen == pentime:
        drpen.goto(0,-300)
        drpen.write(f"Time: {timer}", False, "Center", ("Comic Sans MS", 30, "normal"))
    elif drpen == pen:
        drpen.goto(0,300)
        drpen.write(f"Score: {clickCount}", False, "Center", ("Comic Sans MS", 30, "normal"))
# functions - GameLoop ...................
def clock():
    global timer
    updateDisplay(pentime)
    trtlsize = spot.turtlesize()[0]
    if trtlsize > 1: spot.shapesize(trtlsize-0.5)
    timer -= 1
    if timer > 0: wn.ontimer(clock,1000)
    else: #Reset Game
        spot.hideturtle()
        pen.clear()
        pentime.clear()
        pen.write(f"Game over. You Scored {clickCount} points!", False, "Center", ("Comic Sans MS", 30, "normal")) 
        insertScore(clickCount)
        printScores()
        wn.ontimer(waitBeforeShowingTheResetButton,1000)
def spotRandDisplay():
    if random.randint(0,5) == 1: spot.shape(alonzo)
    else: spot.shape("circle")
    spot.onclick(spotClick)
def rndcycle():
    global timer
    spotRandDisplay()
    spot.goto(random.randint(-350,350),random.randint(-275,275))
    if timer >0: wn.ontimer(rndcycle,random.randint(100,2000))
def spotClick(x,y):
    global clickCount
    global timer
    if timer > 0:
        clickCount += 1
        trtlsize = spot.turtlesize()[0]
        updateDisplay(pen)
        spotRandDisplay()
        if trtlsize < 10: spot.shapesize(trtlsize+0.5)
        spot.goto(random.randint(-350,350),random.randint(-275,275))
def waitBeforeShowingTheResetButton():
    pentime.goto(0,-150)
    pentime.write("Click to play again.", False, "Center", ("Comic Sans MS", 30, "normal"))
    start.showturtle()
def startgame(x,y):
    global clickCount
    global timer 
    clickCount = 0
    timer = 5
    start.hideturtle()
    spot.showturtle()
    spot.turtlesize(5)
    pen.clear()
    trscore.clear()
    spot.onclick(spotClick)
    getHighScores()
    clock()
    rndcycle()  
# functions - Highscore ...................
def getScore(line):
    return(highScores[line][2])  
def saveScore():
    with open ("assets/leaderboard.txt","w") as file1:
        for i in range(len(highScores)):
            line = highScores[i]
            line = f"{line[0]}, {line[1]}, {line[2]}"
            line = line.replace(" ","")
            line = line.replace(",",", ")
            file1.write(f"{line}\n")
def getHighScores():
    global highScores
    highScores = []
    with open("assets/leaderboard.txt","r") as file1:
        for line in file1:
            line = line.strip()
            tmplist = line.split(",")
            highScores.append([tmplist[0], tmplist[1], tmplist[2]])
def insertScore(value):
    global highScores
    for i in range(len(highScores)):
        score = int(getScore(i))
        if value >= score:
            trscore.goto(0,-300)
            trscore.write("You Placed in the Leaderboard!", False, "Center", ("Comic Sans MS", 30, "normal"))
            highScores.insert(i,[i+1, name, str(value)])
            if len(highScores) > 5:
                highScores.pop()
            index = 1
            for line in highScores:
                line[0]= str(index)
                #line = f"{line[0]}, {line[1]}, {line[2]}"
                index += 1
            saveScore()
            break
#innitialize ...................
start.onclick(startgame)
start.shapesize(8)
spot.shapesize(5)
spot.hideturtle()
spot.penup()
spot.speed(10)
spot.onclick(spotClick)
pen.hideturtle()
pen.penup()
pen.speed(0)
pen.color("dimgray")
pen.goto(0,100)
pen.write("Click to Play!", False, "Center", ("Comic Sans MS", 30, "normal"))
pentime.hideturtle()
pentime.penup()
pentime.speed(0)
pentime.color("dimgray")
trscore.hideturtle()
trscore.penup()
trscore.speed(0)
trscore.color("dimgray")
print("Your Game is Running")
wn.mainloop()

