import turtle as trtl, math

wn = trtl.Screen()
wn.tracer(False)

DEBUG_2D = False

SCALE = 1

FOV = 50

r1 = False
r2 = False
r3 = False
r4 = False



plr = trtl.Turtle(visible=DEBUG_2D,shape="turtle")
plr.penup()

pen = trtl.Turtle(visible=False)

pen.penup()
pen.pensize(30)

trace = trtl.Turtle(visible=False)
trace.penup()


wallh = []
wallv = []
wallp = []
wallg = []
wallpoints = [wallh,wallv,wallp,wallg]


def createpoint(pos,dest=wallpoints[3]):
    temp = trtl.Turtle(visible=DEBUG_2D,shape="circle")
    temp.penup()
    temp.goto(pos)
    dest.append(temp)

def createwall(pointA,pointB,ptype=0,step=SCALE):
    trace.goto(pointA)
    trace.setheading(math.degrees(math.atan2((pointB[1]-pointA[1]),(pointB[0]-pointA[0]))))
    distance = 0
    destination = trace.distance(pointB)
    while distance < destination:
        trace.forward(step)
        distance += step
        createpoint(trace.pos(),wallpoints[ptype])
    wn.update()





createwall((-200,100), (100,100), 0)
createwall((-100,50), (-100,-100), 1)
createwall((-100,50), (-200,50), 0)
createwall((100,50), (200,50), 0)
createwall((100,100), (100,200), 1)
createwall((200,50), (200,0), 1)
createwall((200,-50), (200,-100), 1)
createwall((250,-100), (250,200), 1)
createwall((-200,50), (-200,-100), 1)
createwall((-250,-100), (-250,200), 1)
createwall((-200,200), (0,200), 0)
createwall((0,0),(150,0),0)
createwall((150,0),(150,-100),0)

createwall((-100,100), (-100,150), 1)
createwall((-50,125), (-50,150), 1)
createwall((-100,150), (-50,150), 1)

createpoint((-75,125))

wn.update()

plr.goto(0,50)


def updatescreen():
    if not DEBUG_2D:
        pen.clear()
        grouppoints = []
        for list in wallpoints:
            grouppoints += list 
        grouppoints = sorted(grouppoints,key=plr.distance,reverse=True)
        for tr in grouppoints:
            diffx = (tr.xcor()-plr.xcor())
            diffy = (tr.ycor()-plr.ycor())
            plrdist = plr.distance(tr)
            if plrdist < 250:
                pointangle = math.degrees(math.atan2(diffy,diffx))
                diff = (pointangle-plr.heading()+180)%360-180

                wnyscale = wn.window_height()*0.8
                wnxscale = wn.window_width()

                dist = plrdist/12 * math.cos(math.radians(pointangle-plr.heading()))
                if dist < 0: dist = 0

                whi = 0.01 * ((plrdist*0.05)**2) -0.2
                if whi < 0: whi = 0

                r,g,b = [0,0,0]
                if tr in wallpoints[0]: b= 0.05 - 0.1* whi
                if tr in wallpoints[1]: g=0.05 - 0.1* whi
                if tr in wallpoints[2]: g,b = [0.02- 0.1* whi,0.02- 0.1* whi]
                if tr in wallpoints[3]: r,g = [0.4- 0.2* whi,0.3- 0.2* whi]

                r += whi
                if r > 1: r = 1         
                g += whi
                if g > 1: g = 1
                b += whi
                if b > 1: b = 1

                if tr in wallg: dist *= 2

                if not abs(diff) > FOV and dist != 0:
                    pen.pensize(10*(wnxscale/16)/plrdist+20)
                    pen.color(r,g,b)
                    pen.goto(-(((diff+FOV)/(2*FOV))*wnxscale)+(wnxscale/2),wnyscale/dist)
                    pen.pendown()
                    pen.sety(-wnyscale/dist)
                    pen.penup()
    wn.update()




def turnleft():
    if r1:
        plr.left(10)
        updatescreen()
        wn.ontimer(turnleft,50)

def turnright():
    if r2:
        plr.right(10)
        updatescreen()
        wn.ontimer(turnright,50)

def walk():
    if r3:
        prevpos = plr.pos()
        plr.forward(10)
        collide = False
        for list in wallpoints:
            for tr in list:
                if tr in wallg and plr.distance(tr) < 20:
                    print(True)
                if plr.distance(tr) < 10:
                    if tr in wallh: collide = "h"
                    elif tr in wallv: collide = "v"
                    else: collide = True
        if collide == "h": plr.setx(plr.xcor()+(plr.xcor()-prevpos[0]))
        elif collide == "v": plr.sety(plr.ycor()+(plr.ycor()-prevpos[1]))
        if collide:
            plr.back(10)
            for list in wallpoints:
                for tr in list:
                    if plr.distance(tr) < 10: plr.goto(prevpos)
        updatescreen()
        wn.ontimer(walk,50)
        

    

def backwalk():
    if r4:
        prevpos = plr.pos()
        plr.back(10)
        collide = False
        for list in wallpoints:
            for tr in list:
                if tr in wallg and plr.distance(tr) < 20:
                    print(True)
                if plr.distance(tr) < 10:
                    if tr in wallh: collide = "h"
                    elif tr in wallv: collide = "v"
                    else: collide = True
        if collide == "h": plr.setx(plr.xcor()+(plr.xcor()-prevpos[0]))
        elif collide == "v": plr.sety(plr.ycor()+(plr.ycor()-prevpos[1]))
        if collide:
            plr.forward(10)
            for list in wallpoints:
                for tr in list:
                    if plr.distance(tr) < 10: plr.goto(prevpos)
        updatescreen()
        wn.ontimer(backwalk,50)

def startup(procedure,inp):
    global r1,r2,r3,r4
    if inp == 0:
        r1 = True
    elif inp == 1:
        r2 = True
    elif inp == 2:
        r3 = True
    elif inp == 3:
        r4 = True
    wn.onkeypress(None,buttons[inp])
    procedure()

def stoppress(inp):
    global r1,r2,r3,r4
    if inp == 0:
        r1 = False
    elif inp == 1:
        r2 = False
    elif inp == 2:
        r3 = False
    elif inp == 3:
        r4 = False
    wn.onkeypress(lambda ins=presscodes[inp],num=inp: startup(ins,num),buttons[inp])
    


updatescreen()

buttons = ["Left","Right","Up","Down"]
presscodes = [turnleft,turnright,walk,backwalk]

for i in range(4):
    wn.onkeypress(lambda ins=presscodes[i],num=i: startup(ins,num),buttons[i])
    wn.onkeyrelease(lambda ins=i:stoppress(ins),buttons[i])

wn.listen()



wn.update()







wn.mainloop()