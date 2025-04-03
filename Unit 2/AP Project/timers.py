## .......... SETUP .......... ##
import turtle as trtl, string, datetime

# setup - screen
wn = trtl.Screen()
trtl.tracer(0)

## ........ FUNCTIONS ........ ##
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


def maketimer(name,end):
    return([name,end])

def getname(timer):
    return(timer[0])

def getend(timer,islist=False):
    return checkvaliddate(timer[1],True) if islist else timer[1]


def savethedate():
    with open ("assets/timers/timerlist.txt","w") as file1:
        for i in range(len(timers)):
            line = timers[i]
            line = f"{line[0]};{line[1]}\n"
            file1.write(f"{line}")

def isleapyear(year):
    return (year%4==0 and year%100!=0) or (year%400==0)


def checkvaliddate(input,returndate=False):
    try:
        dateordering = []
        if "/" in input:
            data = input.split("/") # From user input
            dateordering = [0,1,2]
        elif "-" in input:
            data = input.split("-") # From datetime value
            dateordering = [1,2,0]
        else:
            return False
        if len(data) != 3:
            return False
        month = int(data[dateordering[0]])
        day = int(data[dateordering[1]])
        year = int(data[dateordering[2]])
        if (month-1 not in range(12)) or ( # checks if the inputed date is a real and valid date. Is it a valid month? (1-12)
            day-1 not in range(dayspermonth[month-1] + (1 if (isleapyear(year) and month == 2) else 0) ) # is the day in the month? 
            ) or not (0 <= year <= 10000): # is the year out of bounds
            return False
        if returndate:
            return [month,day,year]
        else:
            return True
    except:
        return False
    

def dayssince0(date):
    days = date[1]
    for y in range(1, date[2]): 
        if isleapyear(y):
            days += 366 
        else:
            days += 365
    for m in range(1, date[0]):
        days += dayspermonth[m-1]
        if m == 2:
            days += 1
    return days

def printtimes(dsplnum = False):
    for i in range(len(timers)):
        time =  dayssince0(checkvaliddate(timers[i][1],True)) - dayssince0(today)
        pen2.write(f"{f"{i+1}. " if dsplnum else ""}{timers[i][0]}: {time} day{"" if time == 1 else "s"} left",False,"center",("Arial",12,"normal"))
        pen2.sety(pen2.ycor()-25)




def addtimer(x,y):
    menucall(0)
    timers.append(maketimer(getInput("Enter name of the timer.",letters),
                            getInput("Enter ending date.\nIn mm/dd/yyyy",numbers,checkvaliddate)))
    savethedate()
    mainmenu()

def edittimer(x,y):
    menucall(0)
    printtimes(True)
    validnums = []
    for i in range(len(timers)):
        validnums.append(str(i+1))
    selection = getInput("Enter the number of the Timer to Edit.",numbers,validnums)
    print(selection)

def deltimer(x,y):
    pass







def editmode(x=0,y=0):
    pen.clear()
    pen2.clear()
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



def mainmenu(x=0,y=0):
    printtimes()
    pen.goto(0,200)
    menucall(1,[[(300,-250)], # positions
                [5], # sizes
                ["Edit"], # texts
                [(300,-325)], # text pos
                [editmode], # procedures
                ])



## ......... SETUP 2 ......... ##
# setup - pen - text writing etcetera
pen = trtl.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0,200)

pen2 = trtl.Turtle()
pen2.hideturtle()
pen2.penup()
pen2.goto(0,200)
# setup - buttons - turtles stored for clicking on later
bts = []
for i in range(10):
    temp = trtl.Turtle(shape="circle")
    temp.penup()
    temp.hideturtle()
    bts.append(temp)
# setup - keyboard - makes lists of validated inputs for player input
letters = list(string.printable) + ["Return","BackSpace"," ","Shift_L","Shift_R"]
numbers = list(string.digits) + ["/","BackSpace","Return","Escape"]


dayspermonth=[31,28,31,30,31,30,30,31,30,31,30,31]
today = checkvaliddate(str(datetime.date.today()),True)



timers = []
with open("assets/timers/timerlist.txt","r") as file1:
        for line in file1:
            line = line.strip()
            tmplist = line.split(";")
            timers.append(tmplist)


mainmenu()

wn.mainloop()
