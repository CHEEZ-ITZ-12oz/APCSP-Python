import turtle as trtl, math, random
# inntialize ..........
wn = trtl.Screen()
wn.tracer(False)


DEBUG_2D = False  # Debug mode. Displays a 2d version of the maze

if not DEBUG_2D: wn.bgcolor("black")


SCALE = 1

FOV = 40 # default 40

RENDERDIST = 150 # default 150

r1 = False # left
r2 = False # right
r3 = False # up
r4 = False # down

plr = trtl.Turtle(visible=DEBUG_2D,shape="turtle")
plr.penup()

pen = trtl.Turtle(visible=False)

pen.penup()
pen.pensize(30)

trace = trtl.Turtle(visible=False)
trace.penup()

number = 0

warping = False

gameover = False

wallh = [] # horizontal walls
wallv = [] # vertical walls
wallp = [] # gimmick walls / posts
wallg = [] # goal points
wallpoints = [wallh,wallv,wallp,wallg]

# functions ...........
def createpoint(pos,dest=wallpoints[3],num=-1): # creates a point and assigns it to a designated list
    if DEBUG_2D:
        temp = trtl.Turtle(visible=DEBUG_2D,shape="circle")
        if dest == wallpoints[1]: temp.color("blue")
        temp.penup()
        temp.goto(pos)
        temp.onclick(lambda x,y,disp=num:print(disp))
    else:
        temp = (pos)
    dest.append(temp)

def createwall(pointA,pointB,ptype=0,step=SCALE): # creates a list of points between two points and assigns it to a dedicated list
    global number
    trace.goto(pointA)
    trace.setheading(math.degrees(math.atan2((pointB[1]-pointA[1]),(pointB[0]-pointA[0]))))
    distance = 0
    destination = trace.distance(pointB)
    number += 1
    while distance < destination:
        trace.forward(step)
        distance += step
        createpoint(trace.pos(),wallpoints[ptype],number)
        




# innitialize map
# outer walls (1-4)
createwall((-300,-300), (300,-300), 0)
createwall((-300,300), (300,300), 0)
createwall((-300,-300), (-300,300), 1)
createwall((300,-300), (300,300), 1)
# the rest of it (5-10)
createwall((-200,100), (100,100), 0)
createwall((-100,50), (-100,-100), 1)
createwall((-100,50), (-200,50), 0)
createwall((100,50), (200,50), 0)
createwall((100,100), (100,200), 1)
createwall((200,50), (200,0), 1)
# 11-20
createwall((200,-50), (200,-100), 1)
createwall((250,-100), (250,200), 1)
createwall((-200,50), (-200,-100), 1)
createwall((-250,-100), (-250,200), 1)
createwall((-200,200), (0,200), 0)

createwall((0,0),(150,0),0)
createwall((150,0),(150,-100),1)
createwall((-100,100), (-100,150), 1)
createwall((-50,125), (-50,150), 1)
createwall((-100,150), (-50,150), 0)
# 21-30
createwall((-200,-100), (-150,-100), 0)
createwall((-100,-50), (-150,-50), 0)
createwall((-200,0), (-150,0), 0)
createwall((100,50), (100,0), 1)
createwall((-25,150), (150,150), 0)

createwall((-50,125), (50,125), 0)
createwall((75,125), (75,100), 1)
createwall((-200,200), (-200,250), 1)
createwall((200,-200), (200,-300), 1)
createwall((200,-200), (250,-200), 0)
# 31-40
createwall((-50,50), (-50,-100), 1)
createwall((50,50), (50,100), 1)
createwall((-50,-50), (100,-50), 0)
createwall((150,-150), (300,-150), 0)
createwall((150,-150), (150,-250), 1)

createwall((200,200), (150,200), 0)
createwall((200,100), (150,100), 0)
createwall((200,150), (250,150), 0)
createwall((200,200), (200,150), 1)
createwall((150,150), (150,100), 1)
# 41-50
for i in range(10): # the random rooms
    isx = random.randint(0,1)
    x1 = random.randint(-275,125)
    y1 = random.randint(-275,-175)
    if isx == 1:
        x2 = x1
        y2 = random.randint(-275,-175)
    else:
        y2 = y1
        x2 = random.randint(-275,125)
    createwall((x1,y1), (x2,y2), isx)
# 51-60
createwall((-150,150), (-150,100), 1)
createwall((-150,250), (250,250), 0)
createwall((50,225), (50,175), 1)



createpoint((-250,250), wallpoints[2])
createpoint((250,-250), wallpoints[2])

createpoint((-75,125))

wn.update()

plr.goto(0,50)

# main procedures.........
def updatescreen():
    if (not DEBUG_2D) or (not gameover): 
        pen.clear()
        grouppoints = []
        for list in wallpoints:
            grouppoints += list
        grouppoints = {item for item in grouppoints if plr.distance(item) < RENDERDIST + 20}  # do not render anything that is out of the view distance
        grouppoints = sorted(grouppoints,key=plr.distance,reverse=True) # organize all points in a list from back to front for layering
        for pt in grouppoints:
            plrdist = plr.distance(pt)
            # angle...
            diffx = (pt[0]-plr.xcor())
            diffy = (pt[1]-plr.ycor())
            pointangle = math.degrees(math.atan2(diffy,diffx)) # angle the plr must be to face the point
            diff = (pointangle-plr.heading()+180)%360-180 # how much the plr must turn to face the point
            # scale...
            wnyscale = wn.window_height()*0.8
            wnxscale = wn.window_width()
            # how tall the point should render, accounting for fisheye effect
            dist = plrdist/12 * math.cos(math.radians(pointangle-plr.heading())) 
            if dist < 0: dist = 0 # any negative values become 0, so they wont get rendered
            if pt in wallg or pt in wallp: dist *= 2 # half the height of goal points
            # color...
            whi = 0.01 * ((((200/RENDERDIST)**2)*(plrdist*0.05))**2) -0.2 # fog increses with distance
            if whi < 0: whi = 0 # any negative values become 0, so the program doesn't error
            if pt in wallh: r,g,b = [1,1,1] # values to add subtle color to different wall types
            elif pt in wallv: r,g,b = [0.9,0.9,0.9]
            elif pt in wallp: r,g,b = [0.4,0.4,0.8]
            elif pt in wallg: r,g,b = [0.7,0.5,0.1] # goal point must be more strongly marked
            else: r,g,b = [0,0,0]
            # add fog strength to each color
            r -= whi
            if r < 0: r = 0
            g -= whi
            if g < 0: g = 0
            b -= whi
            if b < 0: b = 0
            # rendering
            if not abs(diff) > FOV+5 and dist != 0: # only render if withing a certain range of the player (FOV)
                pen.pensize(12*(wnxscale/16)/plrdist+20) # smoother walls when futher away, but cover up closer walls
                pen.color(r,g,b)
                pen.goto(-(((diff+FOV)/(2*FOV))*wnxscale)+(wnxscale/2),wnyscale/dist)
                pen.pendown()
                pen.sety(-wnyscale/dist)
                pen.penup()
    wn.update()

def winscreen(): # display win screen
    pen.clear()
    pen.goto(0,0)
    pen.color("gold")
    pen.write("You Win!",False,"center",("Arial",30,"bold"))
    wn.update()

def bonuscollisions(): # collision detection for win and warp
    global warping, gameover,r1,r2,r3,r4
    for list in wallpoints:
        for tr in list:
            if tr in wallg and plr.distance(tr) < 20: # End
                gameover = True
                r1,r2,r3,r4 = [False,False,False,False]
                for i in range(4):
                    wn.onkeypress(None,buttons[i])
                    wn.onkeyrelease(None,buttons[i])
                wn.ontimer(winscreen,100)
            if tr in wallp and plr.distance(tr) < 15 and not warping: # warppoint
                warping = True
                plr.goto(-plr.pos()[0],-plr.pos()[1])
                plr.setheading(plr.heading()+180)
            elif tr in wallp and warping: # exit warppoint
                warping = False
                for pt in wallp:
                    if plr.distance(pt) < 50:
                        warping = True


def allaround(x,y,step=1): # returns a list of all points step units away (in the 8 cardinal directions)
    diagstep = math.sqrt((step**2)/2)
    return [(x-diagstep,y+diagstep),(x,y+step),(x+diagstep,y+diagstep),
            (x-step,y),(x+step,y),
            (x-diagstep,y-diagstep),(x,y-step),(x+diagstep,y-diagstep)]

def isinwall(): # collision check
    coli = False
    for tr in wallh + wallv:
        if plr.distance(tr) < 10: coli = True
    return coli

def pushout(curx,cury): # moves the player out of walls. 
    runcount = 1
    while runcount < 10: # the magnitude of correction
        out = False
        for pos in allaround(curx,cury,runcount): # move in a circle around collision point until you are out of a wall
            if not out:
                plr.goto(pos)
                if not isinwall(): 
                    out = True
            else: break
        if out: break
        runcount += 1

def turnleft(): # turn left
    if r1:
        plr.left(10)
        updatescreen()
        wn.ontimer(turnleft,10)

def turnright(): # turn right
    if r2:
        plr.right(10)
        updatescreen()
        wn.ontimer(turnright,10)

def walk(): # move forward (on up arrow)
    if r3:
        stepcount = 0
        while stepcount < 3:
            plr.forward(3)
            curx,cury = plr.pos()
            if isinwall(): pushout(curx,cury)
            stepcount += 1
        bonuscollisions()
        updatescreen()
        wn.ontimer(walk,10)


def backwalk(): # move backward (on down arrow)
    if r4:
        stepcount = 0
        while stepcount < 3:
            plr.backward(3)
            curx,cury = plr.pos()
            if isinwall(): pushout(curx,cury)
            stepcount += 1
        bonuscollisions()
        updatescreen()
        wn.ontimer(backwalk,10)

def startup(procedure,inp): # onkeypress
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

def stoppress(inp): # onkeyrelease
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
    

# main .......
# launch controls
updatescreen()

buttons = ["Left","Right","Up","Down"]
presscodes = [turnleft,turnright,walk,backwalk]

for i in range(4):
    wn.onkeypress(lambda ins=presscodes[i],num=i: startup(ins,num),buttons[i])
    wn.onkeyrelease(lambda ins=i:stoppress(ins),buttons[i])

wn.listen()

wn.mainloop()
