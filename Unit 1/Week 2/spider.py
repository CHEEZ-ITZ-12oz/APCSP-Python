import turtle as trtl
pen=trtl

def drawLeg(x,y,angle,rad=250,xtent=60):
    pen.pensize(20)
    pen.setheading(angle+180)
    pen.goto(x,y)
    pen.pendown()
    pen.circle(rad,xtent)
    pen.penup()

def drawEye(x,y):
    pen.goto(x,y)
    pen.pendown()
    pen.color("purple")
    pen.dot(30)
    pen.color("black")
    pen.dot(18)
    pen.penup()

pen.speed(0)
pen.dot(200)
pen.sety(-100)
pen.dot(125)
pen.penup()
drawEye(-30,-130)
drawEye(10,-130)

for i in [-1,1]:
    for j in range(4):
        drawLeg(50*i,(j*15)-20,-j*i*15,200,90*i)

wn = trtl.Screen()
wn.mainloop()