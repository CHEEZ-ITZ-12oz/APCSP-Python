## initialize ..............
import turtle as trtl, random, sys, pygame
from PIL import Image
# "remove" recursion limit
sys.setrecursionlimit(100000)
# setting up the screen
wn = trtl.Screen()
trtl.tracer(0)
pygame.mixer.init()
## initialize variables ............
# filepath shortcuts
A = "assets/mine/audio"
V = "assets/mine/sprites"
# misc turtle shapes
wn.addshape(f"{V}/Reset.gif")
wn.addshape(f"{V}/Loading.gif")
wn.addshape(f"{V}/Shovel.gif")
# booleans
GameStarted = False
isfirstclick = True
# lists
Mines = []
dugtiles = []
tilestate = []
numbercounts = []
# regular stuff / default settings
Minecount = 15
Length = 10
Height = 10
# innitial size
Prevsize = 0
Size = 600/Length
# turtles
nflag = trtl.Turtle(shape=f"{V}/Loading.gif")
reset = trtl.Turtle(shape=f"{V}/Loading.gif")
settings = trtl.Turtle(shape=f"{V}/Loading.gif")
pen = trtl.Turtle(shape=f"{V}/Loading.gif")
# show loading "screen"
trtl.update()
# text inputs
NUMBERS = ["0","1","2","3","4","5","6","7","8","9","BackSpace","Return","Escape"]
# sounds initialize
sounds = []
for soundname in ["0","1","2","3","4","5","6","7","8","flag","gameover","win"]:
    sounds.append(pygame.mixer.Sound(f"{A}/{soundname}.wav"))
# 9 - flag, 10 - gameover, 11 - win

## funcitons ............
# sound playback
def playsounds(ids): # play all sounds in a list
    for sound in ids:
        sounds[sound].play()
    

def resize_convert(image,scale,num): # saves a copy of given image, scaled by scale, and returns the new filepath
    img = Image.open(image)
    size = (int(img.width*scale), int(img.height*scale))
    img = img.resize(size)
    temppath = f"{V}/display/{num}.gif"
    img.save(temppath,"GIF")
    return temppath

def tileresize(): # resize all the files to match the new size
    global tilestate
    if Size/15.5 != Prevsize/15.5:
        tilestate = []
        for i in range(15):
            image = f"{V}/{i}.gif"
            temppath = resize_convert(image,Size/15.5,i)
            tilestate.append(temppath)
            wn.addshape(temppath)
# Closed - 9, Flag - 10, Mine - 11, Wintile - 12, Flagfail - 13, FailClick - 14


def enterUserText(let,message,valids,error): # displays questions and updates the screen on each keyinput
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
        else: # Add valid inputs to the string
            userinput += let

        pen.goto(0,200)
        pen.write(f"{message}\nPress Enter to Finish",False,"center",("Arial", 20, "bold"))
        pen.goto(0,150)
        if userinput == "":
            pen.write("Type here:",False,"center",("Arial", 12, "italic"))
        else:
            pen.write(userinput,False,"center",("Arial", 15, "normal"))
        if alttext: # This prints if an invalid response is entered
            pen.goto(0,100)
            pen.write(error,False,"center",("Arial", 20, "bold"))
    alttext = False
    trtl.update()
    wn.listen()

def getInput(question,Inputs=[],cond=[],errormessage="Invalid Input. Try again."): # in screen based questionare
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
        wn.onkeypress(lambda let=letter, message = question, valids = cond, error = errormessage:enterUserText(let,message,valids,error),letter)
    wn.listen()
    while not stopped: # repeat until the user says to stop
        wn.update()
    pen.clear()
    for letter in Inputs: # unbind all the keys
        wn.onkeypress(None,letter)
    trtl.update()
    return answer



def gamereset(x,y): # when RESET button is clicked
    global GameStarted, Mines, dugtiles, isfirstclick
    
    nflag.clear()
    nflag.showturtle()
    GameStarted=False
    for row in board:
        for tile in row:
            tile.shape(tilestate[9])
    Mines = []
    dugtiles = []
    isfirstclick = True
    nflag.hideturtle()
    displayMinecount()
    trtl.update()
    
    GameStarted=True

def endgame(iswin,row=0,collumn=0):
    
    global GameStarted
    if GameStarted:
        GameStarted = False
        if iswin:
            playsounds([11])
            for tile in Mines:
                board[tile[0]][tile[1]].shape(tilestate[12])
            nflag.clear()
            nflag.write(f"You Win!",False,"center",("Arial",20,"bold"))
        else:
            playsounds([10])
            for line in board:
                for tile in line:
                    if tile.shape() == tilestate[10]:
                        tile.shape(tilestate[13])
            for tile in Mines:
                if board[tile[0]][tile[1]].shape() == tilestate[13]:    
                    board[tile[0]][tile[1]].shape(tilestate[10])
                else:
                    board[tile[0]][tile[1]].shape(tilestate[11])
            board[row][collumn].shape(tilestate[14])
            nflag.clear()
            nflag.write(f"You Lose!",False,"center",("Arial",20,"bold"))
    trtl.update()
    
        
         
def displayMinecount(): # updates the display of how many flags vs how many Mines
    nflag.clear()
    nflag.goto(0,350)
    flagcount=0
    for row in board:
            for tile in row:
                if tile.shape() == tilestate[10]:
                    flagcount+=1
    flag_minesRatio = Minecount-flagcount
    nflag.write(f"Minecount: {flag_minesRatio}/{Minecount} Mines",False,"center",("Arial",15,"bold"))

def allaround(row,collumn):
    return [(row-1,collumn+1),(row,collumn+1),(row+1,collumn+1),
            (row-1,collumn),(row,collumn),(row+1,collumn),
            (row-1,collumn-1),(row,collumn-1),(row+1,collumn-1)]
    




def checksurrounding(row,collumn,plrclick):
    global numbercounts
    if GameStarted:
        if (row,collumn) in Mines:
            endgame(False,row,collumn)
        elif plrclick != "On Demand":
            if plrclick:
                numbercounts = [0]
            numminescheck = 0
            for mine in Mines:
                if mine in allaround(row,collumn):
                    numminescheck += 1
            board[row][collumn].shape(tilestate[numminescheck])
            dugtiles.append((row,collumn))
            if numminescheck not in numbercounts:
                numbercounts.append(numminescheck)
            if numminescheck == 0:
                for tile in allaround(row,collumn):
                    if 0 <= tile[0] < Height and 0 <= tile[1] < Length and tile not in dugtiles:
                        board[tile[0]][tile[1]].shape(tilestate[9])
                        tileclick(0,0,tile[0],tile[1],False)

            if len(dugtiles) == (Length*Height-Minecount):
                trtl.update()
                endgame(True)
            elif plrclick:
                playsounds(numbercounts)
                trtl.update()
        else:
            playsounds(numbercounts)
            trtl.update()




def tileclick(x,y,row,collumn,plrclick):
    global isfirstclick
    if isfirstclick and GameStarted and board[row][collumn].shape() == tilestate[9]:
        isfirstclick = False
        if (Height*Length)-9 <= Minecount:
            firstclicksafespots = [(row,collumn)]
        else:
            firstclicksafespots = allaround(row,collumn)
        for i in range(Minecount):
            while len(Mines) <= i:
                temp1 = random.randint(0,Height-1)
                temp2 = random.randint(0,Length-1)
                if (temp1,temp2) not in Mines and (temp1,temp2) not in firstclicksafespots:
                    Mines.append((temp1,temp2))
        checksurrounding(row,collumn,plrclick)

    elif GameStarted and (row,collumn) not in dugtiles and board[row][collumn].shape() == tilestate[9]:
        checksurrounding(row,collumn,plrclick)
    elif plrclick == "Demand Entry":
        checksurrounding(row,collumn,"On Demand")



def tileflag(x,y,row,collumn):
    if GameStarted:
        if board[row][collumn].shape() == tilestate[9]:
            playsounds([9])
            board[row][collumn].shape(tilestate[10])
        elif board[row][collumn].shape() == tilestate[10]:
            playsounds([9])
            board[row][collumn].shape(tilestate[9])
        displayMinecount()
        trtl.update()
    

def chord(x,y,row,collumn):
    global numbercounts
    if GameStarted:
        flagcounter = 0
        numbercounts = []
        for space in allaround(row,collumn):
            if 0 <= space[0] < Height and 0 <= space[1] < Length:
                if board[space[0]][space[1]].shape() == tilestate[10]:
                    flagcounter += 1
                elif board[space[0]][space[1]].shape() == tilestate[9]:
                    numbercounts = [0]
        if board[row][collumn].shape() == tilestate[flagcounter]:
            for space in allaround(row,collumn):
                if 0 <= space[0] < Height and 0 <= space[1] < Length:
                    tileclick(0,0,space[0],space[1],False)
            tileclick(0,0,row,collumn,"Demand Entry")
                    
def COND_length(inp):
    try:
        num = int(inp)
        if num >= 6: return True
        else: return False
    except:
        if inp == None: return True
        else: return False

def COND_height(inp):
    try:
        num = int(inp)
        if 0 < num <= Length: return True
        else: return False
    except:
        if inp == None: return True
        else: return False

def COND_mines(inp):
    try:
        num = int(inp)
        if num >= 1 and num < (Length*Height): return True
        else: return False
    except:
        if inp == None: return True
        else: return False

def changesettings(x,y): # SETTINGS button stuff
    global Length,Height,Minecount,board,Size,Mines,dugtiles,isfirstclick,GameStarted,Prevsize
    GameStarted=False
    prevvals = (Length,Height,Minecount)
    stopper = False
    nflag.clear()
    for list in board:
        for tr in list:
            tr.hideturtle()
    settings.hideturtle()
    reset.hideturtle()
    trtl.update()

    temp = getInput(f"Enter width of board\nRecommended Size: 10",NUMBERS,COND_length,"Cannot be smaller than 6 tiles wide.")
    if temp == None:
        stopper = True
    else:
        Length = int(temp)
    if not stopper:
        temp = getInput(f"Enter Height of board",NUMBERS,COND_height,f"Must be equal to or smaller than {Length}.")        
        if temp == None:
            stopper = True
        else:
            Height = int(temp)
    if not stopper:
        temp = getInput(f"Enter Minecount\nRecommended count: {int(Length*Height*0.2)}",NUMBERS,COND_mines)
        if temp == None:
            stopper = True
        else:
            Minecount = int(temp)
    
    if not stopper:
        Prevsize = Size
        Size = 600/Length
        
        for list in board:
            for tr in list:
                tr.goto(1000,1000)
                tr.hideturtle()
                tr.onclick(None)
                del tr
        del board
        nflag.clear()
        nflag.showturtle()
        trtl.update()
        
        Mines = []
        dugtiles = []
        isfirstclick = True
        
        tileresize()

        settheboard()
        
    else:
        Length,Height,Minecount = prevvals
        for list in board:
            for tr in list:
                tr.showturtle()
        settings.showturtle()
        reset.showturtle()   
        trtl.update()
        
    GameStarted=True

def settheboard(): # create each board tile and set up lists and functions and such
    global board
    tiles = []
    board = []
    for sqrow in range(Height):
        for square in range(Length):
            temp = trtl.Turtle(shape=tilestate[9])
            temp.penup()
            temp.goto((square*Size)-(Size*(Length/2))+(Size/2),(sqrow*Size)-(Size*(Height/2))-(Size/2))
            temp.onclick(lambda x, y, row=sqrow, collumn=square, plrclick=True: tileclick(x,y,row,collumn,plrclick))
            temp.onclick(lambda x, y, row=sqrow, collumn=square: tileflag(x,y,row,collumn), 3)
            temp.onclick(lambda x, y, row=sqrow, collumn=square: chord(x,y,row,collumn), 2)
            tiles.append(temp)
        board.append(tiles)
        tiles=[]
    tiles=[]
    reset.onclick(gamereset)
    settings.onclick(changesettings)
    nflag.hideturtle()
    settings.showturtle()
    reset.showturtle() 
    displayMinecount()
    trtl.update()


# Figure this out!!!!!!!!!!!!!!



tileresize()



nflag.penup()
nflag.goto(0,350)

reset.shape(f"{V}/Reset.gif")
reset.penup()
reset.goto(-400,-350)

settings.shape(f"{V}/Shovel.gif")
settings.penup()
settings.goto(400,-350)

pen.penup()
pen.goto(0,200)
pen.hideturtle()

board = []

settheboard()

GameStarted=True







wn.mainloop()
