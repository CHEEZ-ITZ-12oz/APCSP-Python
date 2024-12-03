#   a113_flower_alt_color.py
#   This code draws a flower using modulo
#   to alternate every other color
import turtle as trtl

pen = trtl.Turtle()
pen.speed(0)

# stem
pen.color("green")
pen.pensize(15)
pen.goto(0, -150)
pen.setheading(90)
pen.forward(100)
#  leaf
pen.setheading(270)
pen.circle(20, 120, 20)
pen.setheading(90)
pen.goto(0, -60)
# rest of stem
pen.forward(60)
pen.setheading(0)

# change pen
pen.penup()
pen.shape("circle")
pen.turtlesize(2)

# draw flower
pen.goto(20,180)

for petal in range(18):
  pen.right(20)
  pen.forward(30)
  pen.color("darkorchid")
  if petal % 4 == 3:
    pen.color("red")
  elif petal % 2 == 0:
    pen.color("blue")
  pen.stamp()
  
wn = trtl.Screen()
wn.mainloop()