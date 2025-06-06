## .............. initialize ..............
import sys, os
# supress pygame welcome message in terminal
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
# "remove" recursion limit
sys.setrecursionlimit(100000)
# import everything else
import turtle as trtl, random, pygame, math
from PIL import Image
# setting up the screen
wn = trtl.Screen()
wn.bgcolor(0.9,0.9,0.9)
wn.tracer(False)
pygame.mixer.init()
## ............ initialize variables ............
# filepath shortcuts
H = "assets/mine"
A = "assets/mine/audio"
V = "assets/mine/sprites"
# misc turtle shapes
for filename in ["Reset","Settings","Loading","Pen","PenFrame","Clear","Undo","Leaderboard","Rename"]:
    wn.addshape(f"{V}/{filename}.gif")
# turtles
n_flag = trtl.Turtle(shape=f"{V}/Loading.gif",visible=False)
reset = trtl.Turtle(shape=f"{V}/Loading.gif")
settings = trtl.Turtle(shape=f"{V}/Loading.gif")
logic = trtl.Turtle(shape=f"{V}/Loading.gif")
l_board = trtl.Turtle(shape=f"{V}/Loading.gif")
undologic = trtl.Turtle(shape=f"{V}/Loading.gif",visible=False)
clrlogic = trtl.Turtle(shape=f"{V}/Loading.gif",visible=False)
pen = trtl.Turtle(visible=False)
l_pen = trtl.Turtle(visible=False)
# booleans
GameStarted = False
isfirstclick = True
logicdraw = False
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
# drawing vars
drawcount = 0
drawlist = []
# leaderboard vars
NAME = None
G_LEADER = []
l_leader = []
# Timer vars
gametimer = 0
stoptimer = True
# show loading "screen"
wn.update()
# text inputs
NUMBERS = ["0","1","2","3","4","5","6","7","8","9","BackSpace","Return","Escape"]
LETTERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>',
                  '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', 'space', "BackSpace","Return","Escape","Shift_L","Shift_R"]
# sounds initialize
sound8roll = pygame.mixer.Sound(f"{A}/8roll.wav")
sounds = []
for soundname in ["0","1","2","3","4","5","6","7","8","flag","gameover","win"]:
    sounds.append(pygame.mixer.Sound(f"{A}/{soundname}.wav"))
# 9 - flag, 10 - gameover, 11 - win, 12 - write

## ............ funcitons ............
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
        elif let == "space":
            userinput += " "
        elif let not in ["Shift_L","Shift_R"]: # Add valid inputs to the string
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
    wn.update()
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
    wn.update()
    for letter in Inputs:
        wn.onkeypress(lambda let=letter, message = question, valids = cond, error = errormessage:enterUserText(let,message,valids,error),letter)
    wn.listen()
    while not stopped: # repeat until the user says to stop
        wn.update()
    pen.clear()
    for letter in Inputs: # unbind all the keys
        wn.onkeypress(None,letter)
    wn.update()
    return answer

def gamereset(x,y): # when RESET button is clicked
    global GameStarted, Mines, dugtiles, isfirstclick, gametimer, stoptimer
    clearlogic()
    if logicdraw: drawpen()
    n_flag.clear()
    n_flag.showturtle()
    GameStarted=False
    for row in board:
        for tile in row:
            tile.shape(tilestate[9])
    Mines = []
    dugtiles = []
    isfirstclick = True
    stoptimer = True
    gametimer = 0
    n_flag.hideturtle()
    displayInfo(True)
    wn.update()
    
    GameStarted=True

def endgame(iswin,row=0,collumn=0): # triggers upon mineclick or all non-mine tiles clicked
    global GameStarted, stoptimer
    if GameStarted:
        GameStarted = False
        stoptimer = True
        if iswin:
            playsounds([11])
            for tile in Mines:
                board[tile[0]][tile[1]].shape(tilestate[12])
            n_flag.clear()
            n_flag.goto(0,325)
            n_flag.write(f"You Win!",False,"center",("Arial",20,"bold"))
            n_flag.goto(0,275)
            n_flag.write(f"Time: {gametimer}",False,"center",("Arial",13,"normal"))
            score = calcscore(Minecount,(Length*Height),gametimer) # score
            l_leader.append([NAME,score,f"{Length} x {Height} Board - {Minecount} Mines - Time: {gametimer}"]) # local leaderboard is added to global leaderboard when it is opened
            if NAME: updateboard() # add to global leaderboard automatically if a name exists for the player
        else:
            playsounds([10])
            for line in board:
                for tile in line:
                    if tile.shape() == tilestate[10]: # all flags become flag-fails
                        tile.shape(tilestate[13])
            for tile in Mines: # on each mine tile, display mines and correct flage
                if board[tile[0]][tile[1]].shape() == tilestate[13]: # if flag fail, display flag
                    board[tile[0]][tile[1]].shape(tilestate[10])
                else: # otherwise, display missed mine
                    board[tile[0]][tile[1]].shape(tilestate[11])
            board[row][collumn].shape(tilestate[14])
            n_flag.clear()
            n_flag.write(f"You Lose!",False,"center",("Arial",20,"bold"))
    wn.update()
         
def displayInfo(forcedraw=False): # updates the display of how many flags vs how many Mines as well as the game timer
    n_flag.clear()
    n_flag.goto(0,325)
    if GameStarted or forcedraw or logicdraw:
        flagcount=0
        for row in board:
                for tile in row:
                    if tile.shape() == tilestate[10]:
                        flagcount+=1
        flag_minesRatio = Minecount-flagcount
        n_flag.write(f"Minecount: {flag_minesRatio}/{Minecount} Mines",False,"center",("Arial",15,"bold"))
        if logicdraw:
            n_flag.goto(0,350)
            n_flag.write(f"Note-Taking Mode",False,"center",("Arial",14,"bold"))
        if gametimer > 0:
            n_flag.goto(-25,300)
            n_flag.write(f"Timer: {gametimer}",font=("Arial",13,"normal"))

def allaround(row,collumn): # input of a tile position. Returns the 8 tiles around it and itself.
    return [(row-1,collumn+1),(row,collumn+1),(row+1,collumn+1),
            (row-1,collumn),(row,collumn),(row+1,collumn),
            (row-1,collumn-1),(row,collumn-1),(row+1,collumn-1)]
    
def checksurrounding(row,collumn,plrclick): # logic block controlling what happens when a tile is clicked
    global numbercounts
    if GameStarted:
        if (row,collumn) in Mines: # lose if a mine is clicked
            endgame(False,row,collumn)
        elif plrclick != "On Demand":
            if plrclick: # only on the player click (doesnt run if it's opening multiple tiles at once)
                numbercounts = [0] # for sound que
            numminescheck = 0
            for mine in Mines:
                if mine in allaround(row,collumn):
                    numminescheck += 1
            board[row][collumn].shape(tilestate[numminescheck]) # display the number assosiated with the number of surrounding mines
            dugtiles.append((row,collumn))
            if numminescheck not in numbercounts: # if a unique number, add it to the sound que
                numbercounts.append(numminescheck)
            if numminescheck == 0: # automatically click all tiles around a 0
                for tile in allaround(row,collumn):
                    if 0 <= tile[0] < Height and 0 <= tile[1] < Length and tile not in dugtiles:
                        board[tile[0]][tile[1]].shape(tilestate[9])
                        tileclick(0,0,tile[0],tile[1],False)

            if len(dugtiles) == (Length*Height-Minecount): # Win detection
                endgame(True)
            elif plrclick: # only play sounds when all possible tiles have been opened
                if 8 in numbercounts: # unique interaction for 8-tile
                    channel = sound8roll.play()
                    while channel.get_busy():
                        pygame.time.delay(100)
                    playsounds([8])
                else: playsounds(numbercounts)
                wn.update()
            
        else: # this line only runs at the end of a chord to update the screen properly
            playsounds(numbercounts)
            wn.update()

def tileclick(x,y,row,collumn,plrclick): # handle what happens when a tile is clicked
    global isfirstclick, drawcount, stoptimer
    if logicdraw: # draw if in drawing mode instead of clicking tiles
        drawcount = 0
        l_pen.color("gold")
        l_pen.pensize(2)
        l_pen.penup()
        l_pen.goto(x,y)
        l_pen.pendown()
    elif isfirstclick and GameStarted and board[row][collumn].shape() == tilestate[9]: # first click
        isfirstclick = False
        if (Height*Length)-9 <= Minecount: # if there are too many mines, only the first tile can be clicked
            firstclicksafespots = [(row,collumn)]
        else: # guarantee the first tile is a 0
            firstclicksafespots = allaround(row,collumn)
        for i in range(Minecount): # randomly spawn mines
            while len(Mines) <= i:
                temp1 = random.randint(0,Height-1)
                temp2 = random.randint(0,Length-1)
                if (temp1,temp2) not in Mines and (temp1,temp2) not in firstclicksafespots:
                    Mines.append((temp1,temp2))
        checksurrounding(row,collumn,plrclick) # open all surrounding tiles
        stoptimer = False
        timertick()
    elif GameStarted and (row,collumn) not in dugtiles and board[row][collumn].shape() == tilestate[9]: # any other click after the first one
        checksurrounding(row,collumn,plrclick)
    elif plrclick == "Demand Entry": # unique demand entry click that only happens after a chording
        checksurrounding(row,collumn,"On Demand")
    
def tileflag(x,y,row,collumn): # handle what happens when a tile is flagged
    if GameStarted:
        if board[row][collumn].shape() == tilestate[10]:
            playsounds([9])
            board[row][collumn].shape(tilestate[9])
        elif board[row][collumn].shape() == tilestate[9]:
            playsounds([9])
            board[row][collumn].shape(tilestate[10])
        displayInfo()
        wn.update()
    
def chord(x,y,row,collumn): # handle a chording (middle click)
    global numbercounts
    if GameStarted:
        flagcounter = 0
        numbercounts = []
        for space in allaround(row,collumn): # check the number of flags around a space
            if 0 <= space[0] < Height and 0 <= space[1] < Length:
                if board[space[0]][space[1]].shape() == tilestate[10]:
                    flagcounter += 1
                elif board[space[0]][space[1]].shape() == tilestate[9]:
                    numbercounts = [0]
        if board[row][collumn].shape() == tilestate[flagcounter]: # if the number matches the number of the tile, click the rest of the tiles and force a screen update
            for space in allaround(row,collumn):
                if 0 <= space[0] < Height and 0 <= space[1] < Length:
                    tileclick(0,0,space[0],space[1],False)
            tileclick(0,0,row,collumn,"Demand Entry") # force a screen update
                   
def COND_length(inp): # limit to board length
    try:
        num = int(inp)
        if 100 >= num >= 6: return True
        else: return False
    except:
        if inp == None: return True
        else: return False

def COND_height(inp): # limit to board height
    try:
        num = int(inp)
        if 0 < num <= Length: return True
        else: return False
    except:
        if inp == None: return True
        else: return False

def COND_mines(inp): # limit to number of mines
    try:
        num = int(inp)
        if num >= 1 and num < (Length*Height)-1: return True
        else: return False
    except:
        if inp == None: return True
        else: return False

def changesettings(x,y): # SETTINGS button stuff
    global Length,Height,Minecount,board,Size,Mines,dugtiles,isfirstclick,GameStarted,Prevsize,drawcount,drawlist,stoptimer,gametimer
    GameStarted=False
    prevvals = (Length,Height,Minecount) # save in case of cancelation
    stopper = False
    # hide everything
    drawcount = 0
    drawlist = []
    for list in board:
        for tr in list:
            tr.hideturtle()
    settings.hideturtle()
    reset.hideturtle()
    logic.hideturtle()
    undologic.hideturtle()
    clrlogic.hideturtle()
    l_board.hideturtle()
    if logicdraw:
        drawpen()
    n_flag.clear()
    l_pen.clear()
    wn.update()
    # ask the user for inputs: Height, Length, and Minecount
    temp = getInput(f"Enter width of board\nRecommended Size: 10",NUMBERS,COND_length,"Must be between 6 and 100 tiles wide.")
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
    if not stopper: # run if all inputs entered
        Prevsize = Size
        Size = 600/Length
        # refersh the screen to delete any unused turtle and reinitialize
        wn.reset()
        wn.clear()
        wn.tracer(0)
        wn.bgcolor(0.9,0.9,0.9)
        spawnandsetturtles(set=False)
        stoptimer = True
        gametimer = 0
        wn.update()
        Mines = []
        dugtiles = []
        isfirstclick = True
        tileresize()
        spawnandsetturtles(spawn=False)
        settheboard() 
    else: # show everything again and restore settings
        Length,Height,Minecount = prevvals
        for list in board:
            for tr in list:
                tr.showturtle()
        settings.showturtle()
        reset.showturtle()
        logic.showturtle()
        l_board.showturtle()
        displayInfo(True)
        wn.update()
        
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
            temp.ondrag(linedraw)
            temp.onrelease(stopdrawing)
            tiles.append(temp)
        board.append(tiles)
        tiles=[]
    tiles=[]
    reset.onclick(gamereset)
    settings.onclick(changesettings)
    displayInfo(True)
    wn.update()

def drawpen(x=0,y=0): # logic to switch modes between playing and note-taking mode
    global logicdraw, GameStarted
    logicdraw = not logicdraw
    displayInfo(True)
    if logicdraw:
        GameStarted = False
        logic.shape(f"{V}/Pen.gif")
        wn.bgcolor(0.85,0.8,0.7)
    else:
        logic.shape(f"{V}/PenFrame.gif")
        wn.bgcolor(0.9,0.9,0.9)
        GameStarted = True
    wn.update() 

def linedraw(x,y): # puts the pen down for note-taking mode.
    global drawcount
    if logicdraw:
        l_pen.goto(x,y)
        drawcount += 1
        wn.update()

def stopdrawing(x,y): # puts the pen up for note-taking mode.
    if logicdraw:
        l_pen.penup()
        drawlist.append(drawcount)
    if len(drawlist)>0: # if drawings exist, display edit buttons
        undologic.showturtle()
        clrlogic.showturtle()
    wn.update()
        
def undodraw(x,y): # undoes the last drawing
    if drawlist != []:
        for i in range(drawlist[-1]+5):
            l_pen.undo()
        drawlist.pop()
    if drawlist == []: # hide editing buttons if no more drawings exist 
        undologic.hideturtle()
        clrlogic.hideturtle()
    wn.update()

def clearlogic(x=0,y=0): # clear all drawings
    global drawlist, drawcount
    l_pen.clear()
    drawcount = 0
    drawlist = []
    undologic.hideturtle()
    clrlogic.hideturtle()
    wn.update()

def showleaderboard(x=0,y=0): # logic behind the leaderboard button
    global GameStarted,drawcount,drawlist,NAME
    GameStarted=False
    drawcount = 0
    drawlist = []
    # hide everything
    for list in board:
        for tr in list:
            tr.hideturtle()
    settings.hideturtle()
    reset.hideturtle()
    logic.hideturtle()
    undologic.hideturtle()
    clrlogic.hideturtle()
    if logicdraw:
        drawpen()
    n_flag.clear()
    l_pen.clear()
    l_board.hideturtle()
    if not NAME: # ask the user for a name if none exists
        NAME = getInput(f"Welcome to the Leaderboard\nEnter Username to continue.",LETTERS)
        if NAME: NAME = NAME[0:32] # cull name if too long
    if NAME: # display leaderboard
        l_board.showturtle()
        l_board.shape(f"{V}/Undo.gif")
        l_board.goto(-50,-300)
        l_board.onclick(onreturn)
        settings.showturtle()
        settings.shape(f"{V}/Rename.gif")
        settings.goto(100,-300)
        settings.onclick(refreshwithNoName)
        updateboard()
        userfont = ("Arial",12,"normal")
        largest = 0
        for line in G_LEADER:
            name = line[0]
            pen.goto(0,325)
            pen.write(name,True,"left",userfont)
            if pen.xcor() > largest:
                largest = pen.xcor()
        pen.clear()
        rankx = -200
        infox = largest + (rankx + 75)
        pen.setx(rankx-40)
        pen.write(f"username: {NAME}\n\nRANK.  USERNAME",font=userfont)
        pen.setx(infox)
        pen.write(f"SCORE     ",True,"left",font=userfont)
        pen.sety(pen.ycor()-45)
        for i in range(len(G_LEADER)):
            pen.setx(rankx)
            pen.write(f"{i+1}.    {G_LEADER[i][0]}",font=userfont)
            pen.setx(infox)
            pen.write(f"{round(float(G_LEADER[i][1]))}     ",True,"left",font=userfont)
            pen.write(f"Board info: {G_LEADER[i][2]}",font=("Arial",8,"italic"))
            pen.sety(pen.ycor()-25)
    else: # if name input cancelled, return to game
        onreturn()
    wn.update()

def onreturn(x=0,y=0): # return to game
    global GameStarted
    for list in board:
        for tr in list:
            tr.showturtle()
    pen.clear()
    settings.showturtle()
    settings.goto(400,-350)
    settings.shape(f"{V}/Settings.gif")
    settings.onclick(changesettings)
    reset.showturtle()
    logic.showturtle()
    l_board.showturtle()
    l_board.shape(f"{V}/Leaderboard.gif")
    l_board.goto(-400,350)
    l_board.onclick(showleaderboard)
    displayInfo(True)
    wn.update()
    GameStarted=True

def updateboard(): # add all local leaderboards to the global leaderboard and save to a seperate file
    global G_LEADER, l_leader
    newlist = []
    for entree in (l_leader + G_LEADER):
        insert = 0
        if entree[0] == None:
            entree[0] = NAME
        for i in range(len(newlist)):
            if float(newlist[i][1]) > float(entree[1]):
                insert += 1
        newlist.insert(insert,entree)
    G_LEADER = newlist
    l_leader = []
    while len(G_LEADER) > 10:
        G_LEADER.pop(-1)
    with open (f"{H}/leaderboard.txt","w") as file1:
        for line in G_LEADER:
            text = f"{line[0]};;:;\":^^@D':;{line[1]};;:;\":^^@D':;{line[2]}\n"
            file1.write(f"{text}")

def calcscore(mine,tiles,gametime): # calculate scores based on an equasion. (I love desmos 3d)
    mineweight = 2
    tileweight = 1
    timeweight = 0.01
    targetdensity = 0.7
    punishstrength = 5
    smoothness = 0.5
    reductionfactor = 20
    total =  (1/reductionfactor) * (((mine**mineweight) * (tiles**tileweight) * (math.e ** (-punishstrength*((((mine/tiles)-targetdensity)/smoothness)**2))) ) - ((mine*gametime/tiles)**(timeweight*mine)))
    if total <= 0 or (mine/tiles) > targetdensity: # if score is too low (density is too low) or density is too high (over 70% is entirely luck based and requires no skill) return 0
        return 0
    return total

def timertick(): # handle the timer. "Lags" with the game to make it more fair for laggier compluters (totally not a bug)
    global gametimer
    if not stoptimer:
        gametimer = round(gametimer + 0.01, 2)
        displayInfo()
        wn.ontimer(timertick,10)

def refreshwithNoName(x,y): # clear the name and prompt the user for a new one
    global NAME
    NAME = None
    showleaderboard()

def spawnandsetturtles(spawn=True,set=True): # spawn and set turtles to the respective locations and onclick functions
    global n_flag, reset, settings, logic, l_board, undologic, clrlogic, pen, l_pen
    if spawn:
        n_flag = trtl.Turtle(shape=f"{V}/Loading.gif")
        reset = trtl.Turtle(shape=f"{V}/Loading.gif")
        settings = trtl.Turtle(shape=f"{V}/Loading.gif")
        logic = trtl.Turtle(shape=f"{V}/Loading.gif")
        l_board = trtl.Turtle(shape=f"{V}/Loading.gif")
        undologic = trtl.Turtle(shape=f"{V}/Loading.gif",visible=False)
        clrlogic = trtl.Turtle(shape=f"{V}/Loading.gif",visible=False)
        pen = trtl.Turtle(visible=False)
        l_pen = trtl.Turtle(visible=False)
    if set:
        n_flag.penup()
        n_flag.goto(0,350)
        n_flag.hideturtle()

        reset.shape(f"{V}/Reset.gif")
        reset.penup()
        reset.goto(-400,-350)

        settings.shape(f"{V}/Settings.gif")
        settings.penup()
        settings.goto(400,-350)

        pen.penup()
        pen.goto(0,200)

        logic.shape(f"{V}/PenFrame.gif")
        logic.penup()
        logic.goto(400,0)
        logic.onclick(drawpen)

        undologic.shape(f"{V}/Undo.gif")
        undologic.penup()
        undologic.goto(400,-75)
        undologic.onclick(undodraw)

        clrlogic.shape(f"{V}/Clear.gif")
        clrlogic.penup()
        clrlogic.goto(400,-150)
        clrlogic.onclick(clearlogic)

        l_board.shape(f"{V}/Leaderboard.gif")
        l_board.penup()
        l_board.goto(-400,350)
        l_board.onclick(showleaderboard)

## .......... MAIN ............

tileresize() # initialize tiles to their respective size

# grab leaderboard
with open(f"{H}/leaderboard.txt","r") as file1:
    for line in file1:
        line = line.strip()
        tmplist = line.split(f";;:;\":^^@D':;")
        G_LEADER.append(tmplist)
# initialize turtles' locations
spawnandsetturtles(spawn=False)
# set up the board
board = []
settheboard()
# start the game
GameStarted=True
# wn.mainloop()
wn.mainloop()
