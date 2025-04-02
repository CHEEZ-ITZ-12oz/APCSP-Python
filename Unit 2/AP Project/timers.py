import turtle as trtl, string, random

pen = trtl.Turtle()
wn = trtl.Screen()
trtl.tracer(0)

bts = []
for i in range(10):
    temp = trtl.Turtle(shape="circle")
    temp.penup()
    temp.hideturtle()
    bts.append(temp)

pen.hideturtle()
pen.penup()
pen.goto(0,200)

letters = list(string.printable) + ["Return","BackSpace"," ","Shift_L","Shift_R"]
numbers = list(string.digits)
numbers += ["/","BackSpace","Return","Escape"]

dayspermonth=[0,31,28,31,30,31,30,30,31,30,31,30,31]





timers = []
with open("assets/timers/timerlist.txt","r") as file1:
        for line in file1:
            tmplist = line.split(";")
            timers.append(tmplist)






def enterUserText(let,message,valids):
    global stopped, answer, userinput
    alttext = False
    pen.clear()
    if not stopped:
        if let == "Return":
            if type(valids) == type(enterUserText):
                if (lambda inp=userinput:valids(inp))():
                    stopped = True
                    answer = userinput
                else:
                    alttext = True
                    userinput = ""
            elif userinput in valids or valids == []: # edit condition
                stopped = True
                answer = userinput
            else:
                alttext = True
                userinput = ""
        elif let == "BackSpace":
            userinput = userinput[:-1]
        elif let not in ["\t","\n","\r","\x0b","\x0c","Shift_L","Shift_R",";"]:
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
    trtl.update()
    wn.listen()

def getInput(question,Inputs=[],cond=[]):
    global stopped, userinput
    stopped = False
    userinput = ""
    pen.goto(0,200)
    pen.write(f"{question}\nPress Enter to Finish",False,"center",("Arial", 20, "bold")) # edit message
    pen.goto(0,150)
    pen.write("Type here:",False,"center",("Arial", 12, "italic"))
    trtl.update()
    for letter in Inputs:
        wn.onkeypress(lambda let=letter, message = question, valids = cond, :enterUserText(let,message,valids),letter)
    wn.listen()
    while not stopped:
        wn.update()
    pen.clear()
    for letter in Inputs:
        wn.onkeypress(None,letter)
    trtl.update()
    return answer


def maketimer(name,end,start):
    return([name,end,start])

def getname(timer):
    return(timer[0])

def getend(timer,islist=False):
    return checkvaliddate(timer[1],True) if islist else timer[1]

def getstart(timer):
    return(timer[2])


def savethedate():
    with open ("assets/timers/timerlist.txt","w") as file1:
        for i in range(len(timers)):
            line = timers[i]
            line = f"{line[0]};{line[1]};{line[2]}"
            file1.write(f"{line}")


def checkvaliddate(input,returndate=False):
    try:
        data = input.split("/")
        if len(data) != 3:
            return False
        month = int(data[0])
        if month-1 not in range(12):
            print("false")
            return False
        day = int(data[1])
        if day-1 not in range(dayspermonth[month]):
            return False
        year = int(data[2])
        if returndate:
            return([month,day,year])
        else:
            return True
    except:
        return False
    



def addtimer(x,y):
    menucall(0)
    timers.append(maketimer(getInput("Enter name of the timer.",letters),getInput("Enter ending date.\nIn mm/dd/yyyy",numbers,checkvaliddate),"pineapple"))
    savethedate()
    mainmenu(0,0)

def edittimer(x,y):
    pass

def deltimer(x,y):
    pass







def editmode(x,y):
    pen.clear()
    menucall(4,[[(-200,0),(0,0),(200,0),(-300,-250)], # positions
                [7,7,7,5], # sizes
                ["Add Timer","Edit Timer","Delete Timer","Return"], # texts
                [(-200,-100),(0,-100),(200,-100),(-300,-325)], # text pos
                [addtimer,edittimer,deltimer,mainmenu], # procedures
                ])




def menucall(count,data=[]):
    for bt in bts:
        bt.hideturtle()
        bt.clear()
    for i in range(count):
        bts[i].showturtle()
        bts[i].shapesize(data[1][i])
        bts[i].goto(data[3][i])
        bts[i].write(data[2][i],False,"center",("Arial", 15, "normal"))
        bts[i].goto(data[0][i])
        bts[i].onclick(data[4][i])
    trtl.update()



def mainmenu(x,y):
    for line in timers:
        pen.write(line)
        pen.sety(pen.ycor()-50)
    pen.goto(0,200)
    menucall(1,[[(300,-250)], # positions
                [5], # sizes
                ["Edit"], # texts
                [(300,-325)], # text pos
                [editmode], # procedures
                ])


mainmenu(0,0)

wn.mainloop()
