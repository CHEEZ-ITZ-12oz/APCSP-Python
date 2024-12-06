import turtle as trtl
shapes = ["arrow","circle","classic","square","triangle","turtle"]
colors = ["red","orange","yellow","green","blue","purple"]
turtles = []
for j in range (3):
    for i in range(len(colors)):
        temp_tr = trtl.Turtle()
        temp_tr.shape(shapes[i])
        temp_tr.color(colors[i])
        turtles.append(temp_tr)
for i in range(len(turtles)):
    for pen in turtles[i:-1]:
        pen.speed(0)
        pen.pensize(2)
        pen.penup()
        if pen == turtles[i]:
            pen.pendown()
        pen.forward((i*10)+30)
        pen.right(45)
wn = trtl.Screen()
wn.mainloop()