import turtle as trtl
pen = trtl

def drawSquare(size=40,color="black"):
    pen.color(color)
    pen.pendown()
    pen.begin_fill()
    for i in range(4):
        pen.forward(size)
        pen.left(90)
    pen.end_fill()
    pen.penup()

def setColor(numval):
    if numval%2 == 0: return col1
    else: return col2

def drawRow(y,size,startval):
    pen.goto(-size*4,y)
    for i in range(8):
        drawSquare(size,setColor(startval+i%2))
        pen.forward(size)


pen.penup()
pen.speed(0)
col1 = "red"
col2 = "black"
side = 80

for i in range(8):
    drawRow((i*side)-(side*4),side,i)

wn = trtl.Screen()
wn.mainloop()
