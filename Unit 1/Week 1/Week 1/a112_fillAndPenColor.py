# import turtle module
import turtle as trtl

# create turtle object
pen = trtl.Turtle()

# set the pen and fill colors, then draw a circle
pen.pensize(5)
pen.color("red","green")
pen.begin_fill()
pen.circle(100)
pen.end_fill()
# move the turtle to another part of the screen
pen.penup()
pen.goto(140,140)
pen.pendown()
# change both the pen and fill colors, then draw a polygon of your choice
pen.color("blue","yellow")
pen.begin_fill()
pen.circle(75,steps=5)
pen.end_fill()
# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()