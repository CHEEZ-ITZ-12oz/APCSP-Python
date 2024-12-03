# import the turtle module
import turtle as trtl

# create the turtle object
pen = trtl.Turtle()

print("making a circle...")

# ask user for a color (such as red, green, blue, pink, purple)
col = input("Enter a color: ")

# ask user for the radius of a circle
rad = int(input("Enter a radius: "))

# draw a circle with the radius and line color entered by the user
pen.color(col)
pen.circle(rad)

# get the screen object and make it persist
wn = trtl.Screen()
wn.mainloop()