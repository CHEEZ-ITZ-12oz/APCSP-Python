#   a113_forward_and_right.py
import turtle as trtl

pen = trtl.Turtle()

# Add code to make the turtle move forward 20 pixels
# and then turn right 20 degrees
for i in range(8):
    pen.forward(45)
    pen.right(45)

wn = trtl.Screen()
wn.mainloop()
