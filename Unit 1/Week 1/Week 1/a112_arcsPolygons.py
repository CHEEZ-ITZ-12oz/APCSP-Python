# import turtle module
import turtle as trtl
# create turtle object
pen = trtl.Turtle()
# Add code here for a circle
pen.circle(50)
# move the turtle to another part of the screen
pen.penup()
pen.goto(30,-30)
pen.pendown()
# add code here for an arc
pen.circle(60,45)
# move the turtle to another part of the screen
pen.penup()
pen.goto(-130,130)
pen.pendown()
# add code here for an arc that is greater than 90 degrees and has 5 steps
pen.circle(125,140,5)
# move the turtle to another part of the screen
pen.penup()
pen.goto(150,50)
pen.pendown()
# add code here to create a polygon of your choice using the circle method
pen.circle(75,steps=5)
# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()