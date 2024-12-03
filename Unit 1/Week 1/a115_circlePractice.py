# import turtle module
import turtle as trtl

# create turtle object
pen = trtl.Turtle()
pen.pensize(5)

# move turtle without marking a line
pen.penup()
pen.goto(0, -20)
pen.pendown()

# draw a semi-circle
pen.circle(100, 180)

# move turtle without marking a line
pen.penup()
pen.goto(0, 20)
pen.pendown()

# draw a 3-step semi-circle
pen.circle(100, 180, 3)

# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()