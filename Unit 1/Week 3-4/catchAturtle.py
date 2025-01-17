import turtle as trtl
import random
#setup
wn = trtl.Screen()
spot = trtl.Turtle(shape="circle")
pen = trtl.Turtle()
pentime = trtl.Turtle()
start = trtl.Turtle(shape="circle")
clickCount = 0
timer = 0
#functions
def updateDisplay(drpen):
    drpen.clear()
    if drpen == pentime:
        drpen.goto(0,-300)
        drpen.write(f"Time: {timer}", False, "Center", ("Comic Sans MS", 30, "normal"))
    elif drpen == pen:
        drpen.goto(0,300)
        drpen.write(f"Score: {clickCount}", False, "Center", ("Comic Sans MS", 30, "normal"))
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
        pentime.goto(0,-150)
        pentime.write("Click to play again.", False, "Center", ("Comic Sans MS", 30, "normal"))
        start.showturtle()
def rndcycle():
    global timer
    spot.goto(random.randint(-300,300),random.randint(-300,300))
    if timer >0: wn.ontimer(rndcycle,random.randint(100,2000))
def spotClick(x,y):
    global clickCount
    global timer
    if timer > 0:
        clickCount += 1
        trtlsize = spot.turtlesize()[0]
        updateDisplay(pen)
        if trtlsize < 10: spot.shapesize(trtlsize+0.5)
        spot.goto(random.randint(-300,300),random.randint(-300,300))
    
def startgame(x,y):
    global clickCount
    global timer 
    clickCount = 0
    timer = 10
    start.hideturtle()
    spot.showturtle()
    spot.turtlesize(5)
    pen.clear()
    clock()
    rndcycle()
#innitialize
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


wn.mainloop()
