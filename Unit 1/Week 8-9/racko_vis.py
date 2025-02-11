import turtle as trtl, random, string
# setup ................
pen = trtl.Turtle()
wn = trtl.Screen()

INPUTletters = list(string.printable) + ["space"]
for item in ['\t','\n','\r','\x0b','\x0c']:
    INPUTletters.remove(item)
INPUTnum_nums = list(range(10))
INPUTutility = ["Return","BackSpace"]
INPUTdefault = INPUTnum_nums + INPUTutility
INPUTall = INPUTnum_nums + INPUTutility + INPUTletters
deck = list(range(1, 61))
random.shuffle(deck)

# userinput .........................
def enterUserText(let,message,valids,plr):
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
        elif let == "space":
            userinput += " "
        else:
            userinput += let
        if not alttext:
            pen.goto(0,200)
            pen.write(f"{message}",False,"center",("Arial", 20, "bold")) # edit message
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
        if plr != False:
            display(plr)

    alttext = False
    wn.listen()

def getInput(question,cond,Inputs=INPUTdefault,display=False):
    global stopped, userinput
    stopped = False
    userinput = ""
    pen.goto(0,200)
    pen.write(f"{question}",False,"center",("Arial", 20, "bold")) # edit message
    pen.goto(0,150)
    pen.write("Type here:",False,"center",("Arial", 12, "italic"))
    for letter in Inputs:
        wn.onkeypress(lambda let=letter, message = question, valids = cond, plr = display :enterUserText(let,message,valids,plr),letter)
    wn.listen()
    while not stopped:
        pen.goto(0,0)
    for letter in Inputs:
        wn.onkeypress(donothing,letter)
    wn.listen()
    pen.clear()
    return answer
# functions ..............
def donothing():
    1+1==2

def display(plr):
    pen.goto(0,-200)
    if plr == 1: 
        pen.write(f"Player 1's Turn\nCurrent rack: {rack1}\nTop of Discard Pile: {discard[0]}",
                  False,"center",("Arial", 13, "normal"))
    else:
        pen.write(f"Player 2's Turn\nCurrent rack: {rack2}\nTop of Discard Pile: {discard[0]}",
                  False,"center",("Arial", 13, "normal"))
        
def cardInsert(card,plr):
    global rack1, rack2, discard
    display(plr)
    valids = []
    if plr == 1:
        for val in rack1:
            valids.append(str(val))
    else:
        for val in rack2:
            valids.append(str(val))
    choice = int(getInput(f"Player {str(plr)}\nEnter number to replace with {card}", valids, INPUTdefault, plr))

    if plr == 1:
        idx = rack1.index(choice)
        discard.insert(0,rack1[idx])
        rack1[idx] = card
        for stall in range(20):
            rack1 = rack1
        getInput(f"Player 1\nYour new rack is: {rack1}\nPress Enter to continue",[],INPUTall)
    else:
        idx = rack2.index(choice)
        discard.insert(0,rack2[idx])
        rack2[idx] = card
        for stall in range(20): 
            rack2 = rack2
        getInput(f"Player 2\nYour new rack is: {rack2}\nPress Enter to continue",[],INPUTall)

def wincheck(rack):
    rackCheck = rack[::1]
    rackCheck.sort()
    if rack == rackCheck:
        return True
    else:
        return False

def getRack(size):
    global deck
    listicle = []
    for i in range(size):
        insert = deck.pop(0)
        listicle.append(insert)
    while wincheck(listicle):
        random.shuffle(listicle)
    return(listicle)

def turn(plr):
    global deck, discard
    pen.clear()
    display(plr)
    choice = getInput(f"Player {str(plr)}\nEnter nothing to draw from the Deck.\nEnter anything to draw from Discard.",[],INPUTall,plr)
    if choice == "":
        display(plr)
        card = deck.pop(0)
        choice = getInput(f"Player {str(plr)}\nDrawn Card: {card}\nEnter nothing to Keep." + 
                          "\nEnter anything to Discard.",[],INPUTall, plr)
        if choice == "":
            cardInsert(card,plr)
        else:
            discard.insert(0,card)
    else:
        card = discard.pop(0)
        cardInsert(card,plr)
# main ...................
pen.penup()
pen.speed(0)
pen.hideturtle()

rSize = int(getInput("Enter the size of the rack.\n(Between 5 and 10)",["5","6","7","8","9","10"]))

rack1 = getRack(rSize)
rack2 = getRack(rSize)
discard = [deck.pop(0)]
discard.append(deck.pop(0))

while True:
    turn(1)
    if wincheck(rack1):
        pen.goto(0,0)
        pen.clear()
        pen.write(f"Player 1 Wins!\n{rack1}",False,"center",("Arial", 23, "bold"))
        break
    turn(2)
    if wincheck(rack2):
        pen.goto(0,0)
        pen.clear()
        pen.write(f"Player 1 Wins!\n{rack2}",False,"center",("Arial", 23, "bold"))
        break

wn.mainloop()
