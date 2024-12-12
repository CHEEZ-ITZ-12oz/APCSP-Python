import turtle as trtl
import random
#setup
wn = trtl.Screen()
spot = trtl.Turtle(shape="circle")
pen = trtl.Turtle()
start = trtl.Turtle(shape="circle")
clickCount = 0
timer = 60
#functions
def updateDisplay():
    pen.clear()
    pen.goto(0,-200)
    pen.write(f"Time: {timer}", False, "Center", ("Comic Sans MS", 30, "normal"))
    pen.goto(0,200)
    pen.write(f"Score: {clickCount}", False, "Center", ("Comic Sans MS", 30, "normal"))
def countdown():
    global timer
    updateDisplay()
    timer -= 1
    if timer > 0: wn.ontimer(countdown,1000)
    else:
        print()
def spotClick(x,y):
    global clickCount
    clickCount += 1
    updateDisplay()
    spot.goto(random.randint(-300,300),random.randint(-300,300))
    
def startgame(x,y):
    start.hideturtle()
    spot.showturtle()
    countdown()
#main

start.onclick(startgame)
spot.shapesize(5)
spot.hideturtle()
spot.penup()
spot.speed(0)
spot.onclick(spotClick)
pen.hideturtle()
pen.penup()
pen.speed(0)
pen.color("dimgray")














wn.mainloop()
