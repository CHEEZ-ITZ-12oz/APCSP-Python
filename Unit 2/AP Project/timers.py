## .......... SETUP .......... ##
import turtle as trtl, string, datetime
# setup - screen and assets ...........
wn = trtl.Screen()
trtl.tracer(0)
wn.bgcolor((0.9),(0.9),(0.9))
assets = {}
for names in ["menu","add","edit","delete","return","on","off","name","date","yes","no"]:
    wn.addshape(f"assets/timers/{names}.gif")
    assets[names] = f"assets/timers/{names}.gif"
## ........ FUNCTIONS ........ ##
# functions - userinput...........
def enterUserText(let,message,valids):
    global stopped, answer, userinput
    alttext = False
    pen.clear()
    if not stopped: # repeat until the user says to stop
        if let == "Return":
            if type(valids) == type(enterUserText): # if a function is passed in, run the input through it and evaluate the result
                if (lambda inp=userinput:valids(inp))(): # valid
                    stopped = True
                    answer = userinput
                else: # invalid
                    alttext = True
                    userinput = ""
            elif userinput in valids or valids == []: # valid, all are valid if no valids are defined
                stopped = True
                answer = userinput
            else: # invalid
                alttext = True
                userinput = ""
        elif let == "BackSpace": # remove last input
            userinput = userinput[:-1]
        elif let == "Escape": # Returns None
            stopped = True
            answer = None
        elif let not in ["\t","\n","\r","\x0b","\x0c","Shift_L","Shift_R",";"]: # Add valid inputs to the string
            userinput += let
        if not alttext: # Updates every keypress
            pen.goto(0,200)
            pen.write(f"{message}\nPress Enter to Finish",False,"center",("Arial", 20, "bold"))
            pen.goto(0,150)
            if userinput == "":
                pen.write("Type here:",False,"center",("Arial", 12, "italic"))
            else:
                pen.write(userinput,False,"center",("Arial", 15, "normal"))
        else: # This prints if an invalid response is entered
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
    pen.clear()
    pen.goto(0,200)
    pen.write(f"{question}\nPress Enter to Finish",False,"center",("Arial", 20, "bold"))
    pen.goto(0,150)
    pen.write("Type here:",False,"center",("Arial", 12, "italic"))
    trtl.update()
    for letter in Inputs:
        wn.onkeypress(lambda let=letter, message = question, valids = cond, :enterUserText(let,message,valids),letter)
    wn.listen()
    while not stopped: # repeat until the user says to stop
        wn.update()
    pen.clear()
    for letter in Inputs: # unbind all the keys
        wn.onkeypress(None,letter)
    trtl.update()
    return answer
# functions - filesave...........
def savethedate():
    with open ("assets/timers/timerlist.txt","w") as file1:
        for i in range(len(Timers)):
            line = Timers[i]
            line = f"{line[0]};{line[1]}\n"
            file1.write(f"{line}")
# functions - time formatting / time checking...........
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
            day-1 not in range(DAYSpMONTH[month-1] + (1 if (isleapyear(year) and month == 2) else 0) ) # is the day in the month? 
            ) or not (0 <= year <= 10000): # is the year out of bounds
            return False
        if returndate:
            return [month,day,year]
        else:
            return True
    except:
        return False
# functions - calculations...........
def dayssince0(date): # calculates the ammount of days since year 0
    days = date[1]
    for y in range(0, date[2]): # all numbers from 1 to the current year
        if isleapyear(y):
            days += 366 
        else:
            days += 365
    for m in range(0, date[0]): # all numbers from 0 to the current month
        days += DAYSpMONTH[m]
        if m == 1 and isleapyear(date[2]): # account for leapdays
            days += 1
    return days
# functions - display...........
def menucall(data=[]):
    pen.clear() 
    pen2.clear()
    for bt in bts:
        bt.hideturtle()
        bt.clear()
    for i in range(len(data)):
        bts[i].showturtle()
        bts[i].shape(assets[(data[i][1])])
        bts[i].goto(data[i][3])
        bts[i].write(data[i][2],False,"center",("Arial", 15, "normal"))
        bts[i].goto(data[i][0])
        bts[i].onclick(data[i][4])
    trtl.update()

def printtimes(dsplnum = False):
    pen2.goto(0,325)
    pen2.write("Timers" if not dsplnum else "",False,"center",("Arial",18,"bold"))
    pen2.sety(100 if dsplnum else 300)
    for i in range(len(Timers)):
        time = dayssince0(checkvaliddate(Timers[i][1],True)) - dayssince0(TODAY)
        pen2.write(f"{f"{i+1}. " if dsplnum else ""}{Timers[i][0]}{f": {time} day{"" if time == 1 else "s"} left" if not dsplnum else ""}{f" - \"{Timers[i][1]}\"" if datetoggle else ""}",False,"center",("Arial",12,"normal"))
        pen2.sety(pen2.ycor()-25)

def toggledate(x,y):
    global datetoggle
    datetoggle = not datetoggle
    with open ("assets/timers/settings.txt","w") as file1:
        file1.write(str(datetoggle))
    mainmenu()
## ........... MAIN ........... ##
# main - menus...........
def mainmenu(x=0,y=0):
    menucall([[(300,-250),"menu","Edit",(300,-325),editmode],
              [(-300,-250),"on" if datetoggle else "off","Display Dates?",(-300,-325),toggledate]])
    printtimes()

def editmode(x=0,y=0):
    pen.clear()
    pen2.clear()
    menucall([[(-200,0),"add","Add Timer",(-200,-100),addtimer],
              [(0,0),"edit","Edit Timer",(0,-100),edittimer],
              [(200,0),"delete","Delete Timer",(200,-100),deltimer],
              [(-300,-250),"return","Return",(-300,-325),mainmenu]])
# main - adding a timer...........
def addtimer(x,y):
    menucall()
    while ESCAPECHECK:
        name = getInput("Enter name of the timer.",LETTERS)
        if name == None: break
        date = getInput("Enter ending date.\nIn mm/dd/yyyy",NUMBERS,checkvaliddate)
        if date == None: break
        Timers.append([name,date])
        savethedate()
        break
    mainmenu()
# main - editing a timer...........
def edittimer(x,y):
    menucall()
    printtimes(True)
    validnums = []
    for i in range(len(Timers)):
        validnums.append(str(i+1))
    while ESCAPECHECK:
        selection = getInput("Enter the number of the timer to Edit.",NUMBERS,validnums)
        if selection == None: 
            mainmenu()
            break
        selection = int(selection)-1
        menucall([[(-125,0),"name","Change Name",(-125,-100),lambda x,y,sel=selection:changename(x,y,sel)],
                [(125,0),"date","Change Date",(125,-100),lambda x,y,sel=selection:changedate(x,y,sel)],
                [(300,-250),"return","Return",(300,-325),editmode]])
        pen.write(f"{selection+1}: {Timers[selection][0]}",False,"center",("Arial", 20, "bold"))
        break

def changename(x,y,selection):
    menucall()
    time = getInput("Enter NEW name of the timer.",LETTERS)
    while ESCAPECHECK:
        if time == None: break
        Timers[selection][0] = time
        savethedate()
        break
    mainmenu()

def changedate(x,y,selection):
    menucall()
    date = getInput("Enter NEW ending date.\nIn mm/dd/yyyy",NUMBERS,checkvaliddate)
    while ESCAPECHECK:
        if date == None: break
        Timers[selection][1] = date
        savethedate()
        break
    mainmenu()
# main - deleting a timer...........
def deltimer(x,y):
    menucall()
    printtimes(True)
    validnums = []
    for i in range(len(Timers)):
        validnums.append(str(i+1))
    selection = getInput("Enter the number of the Timer to Delete.",NUMBERS,validnums)
    while ESCAPECHECK:
        if selection == None:
            mainmenu()
            break
        selection = int(selection)-1
        menucall([[(-125,0),"yes","Yes",(-125,-100),lambda x,y,sel=selection:commencedeletion(x,y,sel)],
                [(125,0),"no","No",(125,-100),editmode]])
        pen.write(f"Are you sure you want to delete\n{selection+1}: {Timers[selection][0]}\n(This cannot be undone)",False,"center",("Arial", 20, "bold"))
        break

def commencedeletion(x,y,selection):
    menucall()
    Timers.pop(selection)
    savethedate()
    mainmenu()


## ......... SETUP 2 ......... ##
# setup - pen - text writing etcetera...........
pen = trtl.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0,200)

pen2 = trtl.Turtle()
pen2.hideturtle()
pen2.penup()
pen2.goto(0,200)
# setup - buttons - turtles stored for clicking on later...........
bts = []
for i in range(10):
    temp = trtl.Turtle(shape="circle")
    temp.penup()
    temp.hideturtle()
    bts.append(temp)
# setup - keyboard - makes lists of validated inputs for player input...........
LETTERS = list(string.printable) + ["Return","BackSpace"," ","Escape","Shift_L","Shift_R"]
NUMBERS = list(string.digits) + ["/","BackSpace","Return","Escape"]
# setup - time and date...........
DAYSpMONTH=[31,28,31,30,31,30,30,31,30,31,30,31]
TODAY = checkvaliddate(str(datetime.date.today()),True)
Timers = []
with open("assets/timers/timerlist.txt","r") as file1:
    for line in file1:
        line = line.strip()
        tmplist = line.split(";")
        Timers.append(tmplist)
with open ("assets/timers/settings.txt","r") as file1:
    datetoggle = False
    for line in file1:
        datetoggle = bool(line=="True")
ESCAPECHECK = True

mainmenu()

wn.mainloop()
