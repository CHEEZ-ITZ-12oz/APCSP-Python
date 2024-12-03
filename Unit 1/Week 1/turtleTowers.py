import turtle as trtl
pen = trtl.Turtle()

def drawRect():
    pen.pendown()
    pen.begin_fill()
    for i in range(2):
        pen.forward(100)
        pen.left(90)
        pen.forward(25)
        pen.left(90)
    pen.end_fill()
    pen.penup()

ypos = 0
color_counter = 0
pen.penup()
pen.speed(0)
for i in range(7):
    pen.goto(-175,ypos)
    for j in range(3):
        if color_counter%3 == 0:
            pen.color("red")
        elif color_counter%3 == 1:
            pen.color("green")
        else:
            pen.color("blue")
        drawRect()
        pen.forward(125)
        color_counter += 1
    ypos += 25
    color_counter += 1

wn = trtl.Screen()
wn.mainloop()
