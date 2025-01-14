import turtle as trtl
import string
import random
# setup ...................
apple = trtl.Turtle()
printer = trtl.Turtle()
orderer = trtl.Turtle()
leaderboarder = trtl.Turtle()
wn = trtl.Screen()
# setting default values.........
def_appleY = 290
def_appleDelay = 50
def_appleV = 8
def_appleCount = 5
# var setup .............
letters = list(string.ascii_lowercase)
lettersplus = letters + ["Backspace","Return","Escape"]
lettercall = ""
appleY = def_appleY
appleDelay = def_appleDelay
appleCatchCount = 0
appleskin = "assets/Apple/Appel.gif"
wn.addshape(appleskin)
highScores = []
untilDone = False
playername = ":3"
# funcitons ...............
def donothing():
    1+1
def killGame():
    wn.bye()
def colorPrint(penhue):
    tempvalTextHold = lettercall
    if tempvalTextHold != ":3":
        apple.pencolor(penhue)
        apple.write(tempvalTextHold,False,"center",("Arial",18,"normal"))
        apple.pencolor("black")

def keyread(key):
    global appleY, lettercall, appleCatchCount
    tempvalTextHold = lettercall
    if tempvalTextHold != ":3":
        if key == tempvalTextHold:
            colorPrint("blue")
            appleCatchCount += 1
        else:
            colorPrint("red")
    appleY = -310
    lettercall = ":3"
    fall()

def displayOrder(key):
    global lettercall
    lettercall = key
    orderer.clear()
    orderer.write(lettercall,False,"center",("Arial",30,"bold"))


def fall():
    global appleY, appleDelay, appleCount
    if appleY > -300:
        apple.showturtle()
        appleY -= def_appleV
        apple.sety(appleY)
    elif appleDelay > 0:
        if appleDelay == def_appleDelay: colorPrint("red")
        appleDelay -= 1
        apple.hideturtle()
    else:
        appleCount -= 1
        appleDelay = def_appleDelay
        appleY = def_appleY
        apple.goto(random.randint(-300,300),def_appleY)
        displayOrder(random.choice(letters))

def resetGame():
    global def_appleY, def_appleDelay, def_appleV, def_appleCount, appleCatchCount, appleY, appleDelay
    def_appleY = 290
    def_appleDelay = 50
    def_appleV = 8
    def_appleCount = 5
    appleY = def_appleY
    appleDelay = def_appleDelay
    appleCatchCount = 0
    untilDone = False
    apple.clear()
    orderer.clear()
    printer.clear()
    printer.sety(0)
    printer.write(f"Press 'Enter' to start.\n\nPress 'h' to play in Hard Mode.",False,"center",("Arial",30,"bold"))
    wn.onkeypress(gameStart,"Return")
    wn.onkeypress(hardtrigger,"h")
    wn.bgpic("nopic")
    wn.listen()
# leaderboard .........
def grabLeaderboard():
    global highScores
    highScores = []
    with open("assets/Apple/leaderboard.txt","r") as file1:
        for line in file1:
            line = line.strip()
            tmplist = line.split(",")
            highScores.append([tmplist[0], tmplist[1], tmplist[2]])

def saveLeaderboard():
    with open ("assets/Apple/leaderboard.txt","w") as file1:
        for i in range(len(highScores)):
            line = highScores[i]
            line = f"{line[0]},{line[1]},{line[2]}"
            file1.write(f"{line}\n")


def nameprinter(letter):
    donothing()

def callGetName():
    global untilDone
    leaderboarder.color("green")
    leaderboarder.write("You Placed in the leaderboard!",False,"center",("Arial",20,"bold"))
    leaderboarder.sety(-100)
    
    
    for letter in lettersplus:
        wn.onkeypress(lambda let=letter:nameprinter(let),letter)
    untilDone = False
    
    while untilDone:







        return(">:3c")

def grabScore(line):
    return(highScores[line][2]) 

def callLeaderboardSave(score):
    global highScores
    foundPlace = False
    if len(highScores) == 0:
        highScores = [["1",callGetName(),str(score)]]
        saveLeaderboard()
    else:
        for i in range(len(highScores),0,-1):
            playerScore = int(grabScore(i-1))
            if score > playerScore:
                foundPlace = True
                highScores.insert(i-1,[str(i),callGetName(),str(score)])
                if len(highScores) > 5: highScores.pop()
                index = 1
                for line in highScores:
                    line[0] = str(index)
                    index += 1
                saveLeaderboard()
                break
        if len(highScores) < 5 and not foundPlace:
            highScores.append([str(len(highScores)+1),callGetName(),int(score)])
            saveLeaderboard()




# main (menu) ...........
def gameStart():
    wn.onkeypress(donothing,"Return")
    wn.onkeypress(donothing,"Escape")
    wn.bgpic("assets/Apple/SkyLarge.png")
    global lettercall, appleCount, appleDelay
    appleCount = def_appleCount
    appleDelay = def_appleDelay
    printer.clear()
    for letter in letters:
        wn.onkeypress(lambda let=letter:keyread(let),letter)

    displayOrder(random.choice(letters))
    while appleCount > 0:
        fall()
        wn.listen()
    lettercall = ":3"
    orderer.clear()
    callLeaderboardSave(appleCatchCount)
    orderer.write("Game Over",False,"center",("Arial",24,"bold"))
    printer.sety(100)
    printer.write(f"You Scored {appleCatchCount}/{def_appleCount}\nAccuracy: {(appleCatchCount/def_appleCount)*100}%\nPress 'Enter' to play again.\nPress 'Escape' to quit.",False,"center",("Arial",24,"bold"))
    wn.onkeypress(resetGame,"Return")
    wn.onkeypress(killGame,"Escape")
    wn.listen()

def normaltrigger():
    global def_appleY, def_appleDelay, def_appleV, def_appleCount
    def_appleY = 290
    def_appleDelay = 50
    def_appleV = 8
    def_appleCount = 5
    printer.clear()
    printer.write(f"Press 'Enter' to start.\n\nPress 'h' to play in Hard Mode.",False,"center",("Arial",30,"bold"))
    wn.onkeypress(gameStart,"Return")
    wn.onkeypress(hardtrigger,"h")
    wn.listen()

def hardtrigger():
    global def_appleY, def_appleDelay, def_appleV, def_appleCount
    def_appleY = 250
    def_appleDelay = 5
    def_appleV = 20
    def_appleCount = 20
    printer.clear()
    printer.write(f"Hard Mode\n\nPress 'Enter' to start.\n\nPress 'n' to play in Normal Mode.",False,"center",("Arial",30,"bold"))
    wn.onkeypress(gameStart,"Return")
    wn.onkeypress(normaltrigger,"n")
    wn.listen()



# main ....................
orderer.penup()
orderer.hideturtle()
orderer.goto(0,350)

apple.penup()
apple.shape(appleskin)
apple.shapesize(6)
apple.speed(0)
apple.pencolor("black")
apple.hideturtle()

printer.penup()
printer.hideturtle()

leaderboarder.penup()
leaderboarder.hideturtle()

printer.write(f"Press 'Enter' to start.\n\nPress 'h' to play in Hard Mode.",False,"center",("Arial",30,"bold"))

grabLeaderboard()

wn.onkeypress(gameStart,"Return")
wn.onkeypress(hardtrigger,"h")
wn.listen()


wn.mainloop()








