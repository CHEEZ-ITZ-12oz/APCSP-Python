import turtle as trtl
import random
#setup ...............
name = input("Enter Name: ") # this is here to ask the user before making a screen
#Safely initialize. Error if missing files
try:
    alonzo = "assets/alonzo.gif"
    wn = trtl.Screen()
    wn.addshape(alonzo)
except:
    print(f"\nCould not find assets/alonzo.gif\nPlease make sure the file is in the right place and try again.\n")
    exit()
#check for leaderboard while we are here
try:
    with open("assets/leaderboard.txt","r") as file1:
        reading = file1
except:
    print(f"\nCould not find assets/leaderboard.txt\nPlease make sure the file is in the right place and try again.\n")
    exit()
spot = trtl.Turtle(shape="circle")
pen = trtl.Turtle()
pentime = trtl.Turtle()
start = trtl.Turtle(shape="circle")
trscore = trtl.Turtle()
badtrtl = trtl.Turtle(shape="circle")
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
    if timer > 0:
        drpen.clear()
        if drpen == pentime:
            drpen.goto(0,-300)
            drpen.write(f"Time: {timer}", False, "Center", ("Comic Sans MS", 30, "normal"))
        elif drpen == pen:
            drpen.goto(0,300)
            drpen.write(f"Score: {clickCount}", False, "Center", ("Comic Sans MS", 30, "normal"))
# functions - GameLoop ...................
def clickCheck():
    spot.onclick(spotClick)
    badtrtl.onclick(negClick)
def clock():
    global timer
    updateDisplay(pentime)
    trtlsize = spot.turtlesize()[0]
    if trtlsize > 1: spot.shapesize(trtlsize-0.5)
    timer -= 1
    if timer > 0: wn.ontimer(clock,1000)
    else: #Reset Game
        spot.hideturtle()
        badtrtl.hideturtle()
        pen.clear()
        pentime.clear()
        pen.goto(0,325)
        pen.write(f"Game over. You Scored {clickCount} points!", False, "Center", ("Comic Sans MS", 30, "normal")) 
        insertScore(clickCount)
        printScores()
        wn.ontimer(waitBeforeShowingTheResetButton,1000)
def rndcycle():
    global timer
    clickCheck()
    spot.shape(alonzo)
    spot.goto(random.randint(-350,350),random.randint(-275,275))
    if timer >0: wn.ontimer(rndcycle,random.randint(100,2000))
def rn2cycle():
    global timer
    clickCheck()
    badtrtl.goto(random.randint(-350,350),random.randint(-275,275))
    if timer >0: wn.ontimer(rn2cycle,random.randint(1000,4000))
def spotClick(x,y):
    global clickCount
    global timer
    if timer > 0:
        clickCount += 1
        trtlsize = spot.turtlesize()[0]
        updateDisplay(pen)
        spot.shape(alonzo)
        if trtlsize < 10: spot.shapesize(trtlsize+0.5)
        spot.goto(random.randint(-350,350),random.randint(-275,275))
        if random.randint(1,2) == 1: badtrtl.goto(random.randint(-350,350),random.randint(-275,275))
def waitBeforeShowingTheResetButton():
    pentime.goto(0,-150)
    pentime.write("Click to play again.", False, "Center", ("Comic Sans MS", 30, "normal"))
    start.showturtle()
def startgame(x,y):
    global clickCount
    global timer 
    clickCount = 0
    timer = 10
    start.hideturtle()
    spot.showturtle()
    spot.turtlesize(5)
    badtrtl.showturtle()
    pen.clear()
    trscore.clear()
    spot.onclick(spotClick)
    badtrtl.onclick(negClick)
    badtrtl.speed(0)
    badtrtl.goto(0,-1000)
    badtrtl.speed(10)
    pen.goto(0,300)
    getHighScores()
    clock()
    rndcycle()
    rn2cycle()
    badtrtl.goto(random.randint(-350,350),random.randint(-275,275))
def negClick(x,y):
    global timer
    if timer > 0:
        timer -= 1
        updateDisplay(pentime)
        badtrtl.goto(random.randint(-350,350),random.randint(-275,275))
# functions - Highscore ...................
def getScore(line): return(highScores[line][2]) 
def filterName(rawName):
    rawName = rawName.strip()
    rawName = rawName.replace(" ","//space!//")
    rawName = rawName.replace(",","//comma!//")
    return(rawName)
def unfilterName(filName):
    filName = filName.replace("//space!//"," ")
    filName = filName.replace("//comma!//",",")
    return(filName)
def saveScore():
    with open ("assets/leaderboard.txt","w") as file1:
        for i in range(len(highScores)):
            line = highScores[i]
            nameFilter = line[1]
            nameFilter.strip()
            nameFilter = filterName(nameFilter)
            line = f"{line[0]}, {nameFilter}, {line[2]}"
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
            insertName = tmplist[1]
            insertName = unfilterName(insertName)
            highScores.append([tmplist[0], insertName, tmplist[2]])
def insertScore(value):
    global highScores
    for i in range(len(highScores)):
        score = int(getScore(i))
        if value >=  score:
            trscore.goto(0,-300)
            trscore.write("You Placed in the Leaderboard!", False, "Center", ("Comic Sans MS", 30, "normal"))
            highScores.insert(i,[i+1, name, str(value)])
            if len(highScores) > 5: highScores.pop()
            index = 1
            for line in highScores:
                line[0]= str(index)
                index += 1
            saveScore()
            break
#innitialize ...................
wn.bgcolor(0.9,1,0.95)
start.onclick(startgame)
start.color("lime")
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
badtrtl.shapesize(6)
badtrtl.color("red")
badtrtl.hideturtle()
badtrtl.penup()
badtrtl.speed(0)
badtrtl.goto(0,-1000)
badtrtl.speed(10)
badtrtl.onclick(negClick)
print("Your Game is Running")
wn.mainloop()
