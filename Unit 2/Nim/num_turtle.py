import random, turtle as trtl

pen = trtl.Turtle()
pen2 = trtl.Turtle()
wn = trtl.Screen()

rkshape = "assets/nim/rock.gif"
hlshape = "assets/nim/holo.gif"

wn.addshape(rkshape)
wn.addshape(hlshape)

trtl.tracer(0)
bts = []
for i in range(3):
    temp = trtl.Turtle(shape="circle")
    temp.speed(0)
    temp.shapesize(6)
    temp.penup()
    bts.append(temp)

rks = []
for i in range(20):
    temp = trtl.Turtle(shape=rkshape)
    temp.speed(0)
    temp.penup()
    temp.hideturtle()
    rks.append(temp)

reset = trtl.Turtle(shape="circle")

pen.hideturtle()
pen.speed(0)
pen.penup()

pen2.hideturtle()
pen2.speed(0)
pen2.penup()

reset.hideturtle()
reset.speed(0)
reset.penup()
reset.shapesize(8)


rocks = 20
player1 = True


locations = [(-288,-32),(-224,-32),(-160,-32),(-96,-32),(-32,-32),
             (32,-32),(96,-32),(160,-32),(224,-32),(288,-32),
             (-288,-96),(-224,-96),(-160,-96),(-96,-96),(-32,-96),
             (32,-96),(96,-96),(160,-96),(224,-96),(288,-96)]


def enterUserText(let,message,valids):
    global stopped, answer, userinput
    alttext = False
    pen.clear()
    let = str(let)
    if not stopped:
        if let == "Return":
                if userinput in valids or valids == []: # edit condition
                    stopped = True
                    answer = userinput
                else:
                    alttext = True
                    userinput = ""
        elif let == "BackSpace":
            userinput = userinput[:-1]
        else:
            userinput += let
        if not alttext:
            pen.goto(0,200)
            pen.write(f"{message}\nPress Enter to Finish",False,"center",("Arial", 20, "bold")) # edit message
            pen.goto(0,150)
            if userinput == "":
                pen.write("Type here:",False,"center",("Arial", 12, "italic"))
            else:
                pen.write(userinput,False,"center",("Arial", 15, "normal"))
        else:
            pen.goto(0,200)
            pen.write(f"Invalid Input. Try again.",False,"center",("Arial", 20, "bold"))
            pen.goto(0,150)
            pen.write("Type here:",False,"center",("Arial", 12, "italic"))
    alttext = False
    wn.listen()


def getInput(question,Inputs=[],cond=[]):
    global stopped, userinput
    stopped = False
    userinput = ""
    pen.goto(0,200)
    pen.write(f"{question}\nPress Enter to Finish",False,"center",("Arial", 20, "bold")) # edit message
    pen.goto(0,150)
    pen.write("Type here:",False,"center",("Arial", 12, "italic"))
    for letter in Inputs:
        wn.onkeypress(lambda let=letter, message = question, valids = cond, :enterUserText(let,message,valids),letter)
    wn.listen()
    while not stopped:
        pen.goto(0,0)
    pen.clear()
    return answer

def clearbts():
    pen.clear()
    for bt in bts:
        bt.clear()
        bt.hideturtle()

def clearrks():
    for rk in rks:
        rk.shape(rkshape)
        rk.hideturtle()

def displayrocks():
    trtl.tracer(0)
    for tr in rks:
        tr.hideturtle()
        tr.shape(rkshape)
    for i in range(rocks):
        rks[i].goto(locations[i])
        rks[i].showturtle()
    trtl.update()
    trtl.tracer(1)

def cmpdisp(pull):
    trtl.tracer(0)
    for tr in rks:
        tr.hideturtle()
        tr.shape(rkshape)
    for i in range(rocks+pull):
        rks[i].goto(locations[i])
        if i >= rocks:
            rks[i].shape(hlshape)
        rks[i].showturtle()
    trtl.update()
    trtl.tracer(1)




def runPVP(x,y):
    clearbts()
    displayrocks()
    global player1, rocks
    while True:
        if player1: pull = int(getInput(f"Player 1\nThere are {rocks} rocks. Select 1, 2, or 3 to remove.",["1","2","3","BackSpace","Return"],["1","2","3"]))
        else: pull = int(getInput(f"Player 2\nThere are {rocks} rocks. Select 1, 2, or 3 to remove.",["1","2","3","BackSpace","Return"],["1","2","3"]))
        rocks -= pull
        player1 = not(player1)
        if rocks <= 0:
            break
        displayrocks()
        
    if player1: pen.write(f"Player 1 Wins!",False,"center",("Arial", 20, "bold"))
    else: pen.write(f"Player 2 Wins!",False,"center",("Arial", 20, "bold"))
    restart(0,0)

def runCMP(x,y):
    clearbts()
    displayrocks()
    global player1, rocks
    while True:
        if player1: 
            while True:
                pull = int(getInput(f"There are {rocks} rocks. Select 1, 2, or 3 to remove.",["1","2","3","BackSpace","Return"],["1","2","3"]))
                if pull > 0 and pull <= 3:
                    break
                print("Invalid Input. Try again.")
        else: 
            pull = random.randint(1,3)
            pen2.clear()
            if pull == 1: pen2.write(f"Computer drew 1 rock.",False,"center",("Arial", 20, "bold"))
            else: pen2.write(f"Computer drew {pull} rocks.",False,"center",("Arial", 20, "bold"))
        rocks -= pull
        player1 = not(player1)
        if rocks <= 0:
            break
        if not player1:
            displayrocks()
            for i in range(20000000):
                1+1==2
        else:
            cmpdisp(pull)

    pen2.clear()
    if player1: pen.write(f"Player Wins!",False,"center",("Arial", 20, "bold"))
    else: pen.write(f"Computer Wins!",False,"center",("Arial", 20, "bold"))
    restart(0,0)

def runCMPsmart(x,y):
    clearbts()
    displayrocks()
    global player1, rocks
    while True:
        if player1: 
            while True:
                pull = int(getInput(f"There are {rocks} rocks. Select 1, 2, or 3 to remove.",["1","2","3","BackSpace","Return"],["1","2","3"]))
                if pull > 0 and pull <= 3:
                    break
                print("Invalid Input. Try again.")
        else: 
            if rocks % 4 == 0: pull = 3
            elif rocks % 4 == 3: pull = 2
            elif rocks % 4 == 2: pull = 1
            else: pull = random.randint(1,3)
            pen2.clear()
            if pull == 1: pen2.write(f"Computer drew 1 rock.",False,"center",("Arial", 20, "bold"))
            else: pen2.write(f"Computer drew {pull} rocks.",False,"center",("Arial", 20, "bold"))
        rocks -= pull
        player1 = not(player1)
        if rocks <= 0:
            break
        if not player1:
            displayrocks()
            for i in range(20000000):
                1+1==2
        else:
            cmpdisp(pull)
    pen2.clear()
    if player1: pen.write(f"Player Wins!",False,"center",("Arial", 20, "bold"))
    else: pen.write(f"Computer Wins!",False,"center",("Arial", 20, "bold"))
    restart(0,0)



locs = [(-200,0),(0,0),(200,0)]
cmds = [runPVP,runCMP,runCMPsmart]
prints= ["PvP","Easy Computer","Hard Computer"]


def nimmenu(x,y):
    reset.hideturtle()
    pen.clear()
    reset.clear()
    pen.goto(0,200)
    pen.write(f"Welcome to Nim",False,"center",("Times New Roman", 30, "bold"))
    pen.goto(0,150)
    pen.write(f"Select a difficulty",False,"center",("Arial", 20, "normal"))
    for i in range(len(bts)):
        bts[i].showturtle()
        bts[i].goto(locs[i])
        bts[i].sety(temp.ycor()-120)
        bts[i].write(prints[i],False,"center",("Arial", 15, "normal"))
        bts[i].goto(locs[i])
        bts[i].onclick(cmds[i])
    trtl.update()
    trtl.tracer(1)


def restart(x,y):
    global rocks, player1
    clearrks()
    rocks = 20
    player1 = True
    reset.showturtle()
    reset.goto(0,0)
    reset.write(f"Click to play again",False,"center",("Arial", 15, "normal"))
    reset.goto(0,-100)
    reset.onclick(nimmenu)




nimmenu(0,0)



wn.mainloop()
