import turtle as trtl, random, sys
from PIL import Image

sys.setrecursionlimit(100000) # this line was taken from stackoverflow - https://stackoverflow.com/questions/3323001/what-is-the-maximum-recursion-depth-and-how-to-increase-it

wn = trtl.Screen()
trtl.tracer(0)



c = "assets/mine"
wn.addshape(f"{c}/Reset.gif")
wn.addshape(f"{c}/Loading.gif")
wn.addshape(f"{c}/Shovel.gif")
GameStarted = False
isfirstclick = True


mines = []
dugtiles = []
tilestate = []


minecount = 20
length = 10
height = 10

size = 600/length

pen = trtl.Turtle(shape=f"{c}/Loading.gif")

reset = trtl.Turtle(shape=f"{c}/Loading.gif")

settings = trtl.Turtle(shape=f"{c}/Loading.gif")

trtl.update()

def resize_convert(image,scale,num):
    img = Image.open(image)
    size = (int(img.width*scale), int(img.height*scale))
    img = img.resize(size)
    temppath = f"{c}/temp/{num}.gif"
    img.save(temppath,"GIF")
    return temppath


def tileresize():
    global tilestate
    tilestate = []
    for i in range(15):
        image = f"{c}/{i}.gif"
        temppath = f"{c}/temp/{i}.gif"
        temppath = resize_convert(image,size/15.5,i)
        tilestate.append(temppath)
        wn.addshape(temppath)
# Closed - 9, Flag - 10, Mine - 11, Wintile - 12, Flagfail - 13, FailClick - 14



def gamereset(x,y):
    global GameStarted, mines, dugtiles, isfirstclick
    
    pen.clear()
    pen.showturtle()
    GameStarted=False
    for row in board:
        for tile in row:
            tile.shape(tilestate[9])
    mines = []
    dugtiles = []
    isfirstclick = True
    pen.hideturtle()
    displayMinecount()
    trtl.update()
    
    GameStarted=True

def endgame(iswin,row=0,collumn=0):
    
    global GameStarted
    if GameStarted:
        GameStarted = False
        if iswin:
            for tile in mines:
                board[tile[0]][tile[1]].shape(tilestate[12])
            pen.clear()
            pen.write(f"You Win!",False,"center",("Arial",20,"bold"))
        else:
            for line in board:
                for tile in line:
                    if tile.shape() == tilestate[10]:
                        tile.shape(tilestate[13])
            for tile in mines:
                if board[tile[0]][tile[1]].shape() == tilestate[13]:    
                    board[tile[0]][tile[1]].shape(tilestate[10])
                else:
                    board[tile[0]][tile[1]].shape(tilestate[11])
            board[row][collumn].shape(tilestate[14])
            pen.clear()
            pen.write(f"You Lose!",False,"center",("Arial",20,"bold"))
    trtl.update()
    
        
         
def displayMinecount():
    pen.clear()
    pen.goto(0,350)
    flagcount=0
    for row in board:
            for tile in row:
                if tile.shape() == tilestate[10]:
                    flagcount+=1
    flag_minesRatio = minecount-flagcount
    pen.write(f"Minecount: {flag_minesRatio}/{minecount} mines",False,"center",("Arial",15,"bold"))

def allaround(row,collumn):
    return [(row-1,collumn+1),(row,collumn+1),(row+1,collumn+1),
            (row-1,collumn),(row,collumn),(row+1,collumn),
            (row-1,collumn-1),(row,collumn-1),(row+1,collumn-1)]
    




def checksurrounding(row,collumn,plrclick):
    if GameStarted:
        if (row,collumn) in mines:
            endgame(False,row,collumn)
        else:
            numminescheck = 0
            for mine in mines:
                if mine in allaround(row,collumn):
                    numminescheck += 1
            board[row][collumn].shape(tilestate[numminescheck])
            dugtiles.append((row,collumn))
            if numminescheck == 0:
                for tile in allaround(row,collumn):
                    if 0 <= tile[0] < height and 0 <= tile[1] < length and tile not in dugtiles:
                        board[tile[0]][tile[1]].shape(tilestate[9])
                        tileclick(0,0,tile[0],tile[1],False)
            if plrclick:
                trtl.update()    
            
            if len(dugtiles) == (length*height-minecount):
                endgame(True)




def tileclick(x,y,row,collumn,plrclick):
    global isfirstclick
    if isfirstclick and GameStarted and board[row][collumn].shape() == tilestate[9]:
        isfirstclick = False
        if (height*length)-9 <= minecount:
            firstclicksafespots = [(row,collumn)]
        else:
            firstclicksafespots = allaround(row,collumn)
        for i in range(minecount):
            while len(mines) <= i:
                temp1 = random.randint(0,height-1)
                temp2 = random.randint(0,length-1)
                if (temp1,temp2) not in mines and (temp1,temp2) not in firstclicksafespots:
                    mines.append((temp1,temp2))
        checksurrounding(row,collumn,plrclick)

    elif GameStarted and (row,collumn) not in dugtiles and board[row][collumn].shape() == tilestate[9]:
        checksurrounding(row,collumn,plrclick)
    


def tileflag(x,y,row,collumn):
    if GameStarted:
        if board[row][collumn].shape() == tilestate[9]:
            board[row][collumn].shape(tilestate[10])
        elif board[row][collumn].shape() == tilestate[10]:
            board[row][collumn].shape(tilestate[9])
        displayMinecount()
        trtl.update()
    

def chord(x,y,row,collumn):
    if GameStarted:
        flagcounter = 0
        for space in allaround(row,collumn):
            if 0 <= space[0] < height and 0 <= space[1] < length:
                if board[space[0]][space[1]].shape() == tilestate[10]:
                    flagcounter += 1
        if board[row][collumn].shape() == tilestate[flagcounter]:
            for space in allaround(row,collumn):
                if 0 <= space[0] < height and 0 <= space[1] < length:
                    tileclick(0,0,space[0],space[1],True)
    
            



def changesettings(x,y):
    global length,height,minecount,board,size,mines,dugtiles,isfirstclick,GameStarted
    GameStarted=False
    prevvals = (length,height,minecount)
    stopper = False
    while True:
        try:
            temp = wn.textinput("Enter width of board","Recommended size: 10")
            length = int(temp)
            if length >= 6:
                break
        except:
            if temp == None:
                stopper = True
                break
    if not stopper:
        while True:
            try:
                temp = wn.textinput("Enter height of board",f"Must be equal to or smaller than {length}")
                height = int(temp)
                if 0 < height <= length:
                    break
            except:
                if temp == None:
                    stopper = True
                    break
    if not stopper:
        while True:
            try:
                temp = wn.textinput("Enter minecount",f"   Recommended count: {int(length*height*0.2)}   ")
                minecount = int(temp)
                if minecount >= 1:
                    break
            except:
                if temp == None:
                    stopper = True
                    break
    
    if not stopper:
        size = 600/length
        
        for list in board:
            for tr in list:
                tr.goto(1000,1000)
                tr.hideturtle()
                tr.onclick(None)
                del tr
        del board
        pen.clear()
        pen.showturtle()
        trtl.update()
        
        mines = []
        dugtiles = []
        isfirstclick = True

        tileresize()

        tiles = []
        board = []
        for sqrow in range(height):
            for square in range(length):
                temp = trtl.Turtle(shape=tilestate[9])
                temp.speed(0)
                temp.penup()
                temp.goto((square*size)-(size*(length/2))+(size/2),(sqrow*size)-(size*(height/2))-(size/2))
                temp.onclick(lambda x, y, row=sqrow, collumn=square, plrclick=True: tileclick(x,y,row,collumn,plrclick))
                temp.onclick(lambda x, y, row=sqrow, collumn=square: tileflag(x,y,row,collumn), 3)
                temp.onclick(lambda x, y, row=sqrow, collumn=square: chord(x,y,row,collumn), 2)
                tiles.append(temp)
            board.append(tiles)
            tiles=[]
        tiles=[]
        reset.onclick(gamereset)
        settings.onclick(changesettings)
        pen.hideturtle()
        displayMinecount()
        trtl.update()
        
    else:
        length,height,minecount = prevvals
    
    GameStarted=True




# Figure this out!!!!!!!!!!!!!!



tileresize()



pen.speed(0)
pen.penup()
pen.goto(0,350)

reset.speed(0)
reset.shape(f"{c}/Reset.gif")
reset.penup()
reset.goto(-400,-350)

settings.speed(0)
settings.shape(f"{c}/Shovel.gif")
settings.penup()
settings.goto(400,-350)


tiles = []
board = []
for sqrow in range(height):
    for square in range(length):
        temp = trtl.Turtle(shape=tilestate[9])
        temp.speed(0)
        temp.penup()
        temp.goto((square*size)-(size*(length/2))+(size/2),(sqrow*size)-(size*(height/2))-(size/2))
        temp.onclick(lambda x, y, row=sqrow, collumn=square, plrclick=True: tileclick(x,y,row,collumn,plrclick))
        temp.onclick(lambda x, y, row=sqrow, collumn=square: tileflag(x,y,row,collumn), 3)
        temp.onclick(lambda x, y, row=sqrow, collumn=square: chord(x,y,row,collumn), 2)
        tiles.append(temp)
    board.append(tiles)
    tiles=[]
tiles=[]
reset.onclick(gamereset)
settings.onclick(changesettings)
pen.hideturtle()
displayMinecount()
trtl.update()

GameStarted=True







wn.mainloop()
