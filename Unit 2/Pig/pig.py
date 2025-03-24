import turtle as trtl, random
trtl.tracer(0)
wn = trtl.Screen()


sphit="assets/pig/hit.gif"
sphold="assets/pig/hold.gif"
wn.addshape(sphit)
wn.addshape(sphold)
diceface = []
rdiceface = []
cdiceface = []
for i in range(6+1):
    image = f"assets/pig/{i}.gif"
    diceface.append(image)
    wn.addshape(image)
for i in range(6+1):
    image = f"assets/pig/r{i}.gif"
    rdiceface.append(image)
    wn.addshape(image)
for i in range(6+1):
    image = f"assets/pig/c{i}.gif"
    cdiceface.append(image)
    wn.addshape(image)



bthit = trtl.Turtle(shape=sphit)
bthold = trtl.Turtle(shape=sphold)
ddice = trtl.Turtle(shape=diceface[1])
tt = trtl.Turtle()
p1 = trtl.Turtle()
p2 = trtl.Turtle()
menubuttonnumber1 = trtl.Turtle(shape="circle")
menubuttonnumber2 = trtl.Turtle(shape="circle")
reset = trtl.Turtle(shape="circle")



bthit.penup()
bthit.goto(-200,-200)
bthit.hideturtle()

bthold.penup()
bthold.goto(200,-200)
bthold.hideturtle()

ddice.penup()
ddice.hideturtle()

tt.penup()
tt.goto(0,150)
tt.hideturtle()

p1.penup()
p1.goto(0,300)
p1.hideturtle()

p2.penup()
p2.goto(0,270)
p2.hideturtle()

menubuttonnumber1.penup()
menubuttonnumber1.goto(-200,-150)
menubuttonnumber1.shapesize(10)

menubuttonnumber2.penup()
menubuttonnumber2.goto(200,-150)
menubuttonnumber2.shapesize(10)

reset.penup()
reset.shapesize(8)
reset.hideturtle()

ttotal = 0
tot1 = 0
tot2 = 0
isPlr1 = True
isCMP = False
isitawin = False

turnindicator = {True: "> ",
                 False: ""}
CMPindicator = {True: "Computer",
                 False: "Player 2"}
playerintdicator = {True: lambda: "Player 1",
                False: lambda: CMPindicator.get(isCMP)}
                

def closebts():
    bthit.onclick(None)
    bthold.onclick(None)

def openbts():
    bthit.onclick(hitit)
    bthold.onclick(holdit)

def temphalt(count):
    trtl.tracer(1)
    for i in range(count):
        ddice.goto(0,0)
    trtl.tracer(0)


def hitit(x,y):
    global ttotal
    closebts()
    if x == 100000000000000000 or isPlr1 or not isCMP:
        for i in range(17):
            rnd = random.randint(1,6)
            temphalt(2)
            if isPlr1: ddice.shape(diceface[rnd])
            elif isCMP: ddice.shape(cdiceface[rnd])
            else: ddice.shape(rdiceface[rnd])
            ddice.goto(random.randint(-15,15),random.randint(-15,15))
            trtl.update()
        ddice.goto(0,0)
        if rnd == 1:
            ttotal = 0
            temphalt(50)
            holdit(0,0)
        else:
            ttotal += rnd
        tt.clear()
        tt.write(f"Turn total: {ttotal}",False,"center",("Arial","16","normal"))
        openbts()
        if isPlr1 and ttotal + tot1 >= 100:
            endgame(True)
        elif not isPlr1 and ttotal + tot2 >= 100:
            endgame(False)
        trtl.update()

def holdit(x,y):
    global ttotal, tot1, tot2, isPlr1
    closebts()
    if isPlr1: tot1 += ttotal
    else: tot2 += ttotal
    ttotal = 0
    isPlr1 = not isPlr1
    if isPlr1: ddice.shape(diceface[1])
    elif isCMP: ddice.shape(cdiceface[1])
    else: ddice.shape(rdiceface[1])
    p1.clear()
    p2.clear()
    p1.write(f"{turnindicator.get(isPlr1)}Player 1 score: {tot1}",False,"center",("Arial","16","bold"))
    p2.write(f"{turnindicator.get(not isPlr1)}{CMPindicator.get(isCMP)} score: {tot2}",False,"center",("Arial","16","bold"))
    tt.clear()
    tt.write(f"Turn total: 0",False,"center",("Arial","16","normal"))
    trtl.update()
    if isCMP and not isPlr1:
        closebts()
        while True:
            if not tot2 >= 71 and ttotal >= 21+abs((tot1-tot2)//8):
                break
            hitit(100000000000000000,0)
            closebts()
            if ttotal == 0:
                break
            elif isitawin:
                break
            temphalt(20)
        if ttotal > 0 and not isitawin:
            holdit(0,0)
    openbts()

def endgame(pl1win):
    global isitawin
    isitawin = True
    closebts()
    bthit.hideturtle()
    bthold.hideturtle()
    ddice.hideturtle()
    p1.clear()
    p2.clear()
    tt.clear()
    p1.write(f"{playerintdicator.get(pl1win,lambda:"An error occored")()} Wins!",False,"center",("Arial","20","bold"))
    reset.goto(0,-150)
    reset.write(f"Reset",False,"center",("Arial","14","normal"))
    reset.goto(0,0)
    reset.showturtle()
    reset.onclick(resetandbegin)
    trtl.tracer(0)
    trtl.update()
    
    

def begingame(x,y,type="plr"):
    global isCMP, isitawin, ttotal, tot1, tot2, isPlr1, isCMP
    ttotal = 0
    tot1 = 0
    tot2 = 0
    isPlr1 = True
    isitawin = False
    p1.clear()
    p2.clear()
    menubuttonnumber1.clear()
    menubuttonnumber2.clear()
    menubuttonnumber1.hideturtle()
    menubuttonnumber2.hideturtle()
    menubuttonnumber1.onclick(None)
    menubuttonnumber2.onclick(None)
    bthit.showturtle()
    bthold.showturtle()
    ddice.showturtle()
    if type == "CMP": isCMP = True
    else: isCMP = False
    tt.write(f"Turn total: 0",False,"center",("Arial","16","normal"))
    p1.write(f"> Player 1 score: 0",False,"center",("Arial","16","bold"))
    p2.write(f"{CMPindicator.get(isCMP)} score: 0",False,"center",("Arial","16","bold"))
    bthit.onclick(hitit)
    bthold.onclick(holdit)
    trtl.update()

def resetandbegin(x,y):
    p1.clear()
    reset.clear()
    reset.onclick(None)
    reset.hideturtle()
    menubuttonnumber1.showturtle()
    menubuttonnumber1.goto(-200,-150)
    menubuttonnumber2.showturtle()
    menubuttonnumber2.goto(200,-150)
    p1.write(f"Game of Pig",False,"center",("Arial","20","bold"))
    p2.write(f"Select number of players",False,"center",("Arial","10","normal"))
    menubuttonnumber1.write(f"1 Player",False,"center",("Arial","10","normal"))
    menubuttonnumber1.sety(0)
    menubuttonnumber2.write(f"2 Players",False,"center",("Arial","10","normal"))
    menubuttonnumber2.sety(0)
    menubuttonnumber1.onclick(lambda x, y, type="CMP": begingame(x,y,type))
    menubuttonnumber2.onclick(begingame)
    trtl.update()

resetandbegin(0,0)


wn.mainloop()