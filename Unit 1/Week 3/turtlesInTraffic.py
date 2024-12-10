import turtle as trtl
import random
horiz_turtles = []
vert_turtles = []
turtle_shapes =  ["arrow","circle","square","triangle","turtle"]
horiz_colors = ["red","salmon","lime","blue","purple"]
vert_colors = ["darkred", "orange", "green", "darkblue", "indigo"]



for i in range(len(turtle_shapes)):
    temp_tr = trtl.Turtle()
    temp_tr.shape(turtle_shapes[i])
    temp_tr.color(horiz_colors[i])
    horiz_turtles.append(temp_tr)

for i in range(len(turtle_shapes)):
    temp_tr = trtl.Turtle()
    temp_tr.shape(turtle_shapes[i])
    temp_tr.color(vert_colors[i])
    vert_turtles.append(temp_tr)

ypos=0
xpos=0
hx=[]
hy=[]
vx=[]
vy=[]
for pen in horiz_turtles:
    pen.penup()
    pen.goto(xpos,300)  
    pen.setheading(-90)
    hy.append(300)
    hx.append(xpos)
    xpos += 50
for pen in vert_turtles:
    pen.penup()
    pen.goto(300,ypos)
    pen.setheading(180)
    vy.append(ypos)
    vx.append(300)
    ypos += 50

turncount = 50
while True:
    for i in range(len(horiz_turtles)):
        if horiz_turtles[i]:
            ht = horiz_turtles[i]
            ht.forward(random.randint(1,20))
            hx[i] = ht.xcor()
            hy[i] = ht.ycor()
            if (abs(hx[i] - vx[i]) < 10) and (abs(hy[i] - vy[i]) < 10):
                ht.color("gray")
                vert = vert_turtles[i]
                vert.color("gray")
                for val in [hx,hy,vx,vy,horiz_turtles,vert_turtles]:
                    val[i]=False

    for i in range(len(vert_turtles)):
        if vert_turtles[i]:
            vt = vert_turtles[i]
            vt.forward(random.randint(1,20))
            vx[i] = vt.xcor()
            vy[i] = vt.ycor()
            if (abs(hx[i] - vx[i]) < 10) and (abs(hy[i] - vy[i]) < 10):
                vt.color("gray")
                horz = horiz_turtles[i]
                horz.color("gray")
                for val in [hx,hy,vx,vy,horiz_turtles,vert_turtles]:
                    val[i]=False

    turncount -= 1
    if not vert_turtles or not horiz_turtles or turncount <= 0: break
    

       
wn = trtl.Screen()
wn.mainloop()
