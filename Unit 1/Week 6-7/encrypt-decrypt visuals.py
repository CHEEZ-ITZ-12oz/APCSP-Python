import string, turtle as trtl
# setup..................................
bt1 = trtl.Turtle(shape="circle")
bt2 = trtl.Turtle(shape="circle")
pen = trtl.Turtle()
wn = trtl.Screen()

isEncoding = True
isCaesar = True
stopped = False
stopped2_electricboogaloo = False

allLetters = list(string.printable) + ["Return","BackSpace","space"]
lettersBlacklist = ['\t','\n','\r','\x0b','\x0c']
alphabet = list(string.ascii_lowercase)
numbers = list(string.digits)
cypherbet = []
theUpper_case = []
result = ""
userinput = ""
userkey = ""
textstring = ""
# functions ............................
modetxt = {True: "encode", False: "decode"}
typetxt = {True: "Caesar", False: "Monoalphabetic"}

def donothingdawg():
    pass

def byebye():
    wn.bye()

def fixAlphabet():
    global alphabet
    alphabet = list(string.ascii_lowercase)

def caesarShift(value):
    shifted = alphabet
    for i in range(value):
        shifted.append(shifted.pop(0))
    fixAlphabet()
    return(shifted)

def monoAlphabet(key):
    monolist = list(key)
    reversedAlpha = alphabet[::-1]
    for letter in reversedAlpha:
        if not letter in monolist:
            monolist.append(letter)
    fixAlphabet()
    return(monolist)

def getCase(message):
    messageList = list(message)
    caselist = []
    for letter in messageList:
        if letter.isupper():
            caselist.append(True)
        else: caselist.append(False)
    return(caselist)

def monoReqs(key):
    keylist = list(key)
    for letter in keylist:
        if keylist.count(letter) > 1:
            return(False)
    return(True)

def encode(usertext,alpha,caseread):
    global result
    usertext = usertext.lower()
    usertext = list(usertext)
    endlist = []
    textreader = ""
    letterinsert = ""
    endtext = ""
    for i in range(len(usertext)):
        textreader = usertext[i]
        if textreader in alphabet:
            letterinsert = alpha[alphabet.index(textreader)]
        else:
            letterinsert = textreader
        endlist.append(letterinsert)
    for i in range(len(usertext)):
        textreader = endlist[i]
        if caseread[i]:
            endtext += textreader.upper()
        else:
            endtext += textreader
    result = endtext

def decode(usertext,alpha,caseread):
    global result
    usertext = usertext.lower()
    usertext = list(usertext)
    endlist = []
    textreader = ""
    letterinsert = ""
    endtext = ""
    for i in range(len(usertext)):
        textreader = usertext[i]
        if textreader in alphabet:
            letterinsert = alphabet[alpha.index(textreader)]
        else:
            letterinsert = textreader
        endlist.append(letterinsert)
    for i in range(len(usertext)):
        textreader = endlist[i]
        if caseread[i]:
            endtext += textreader.upper()
        else:
            endtext += textreader
    result = endtext
# trtl Functions ...................
def penWriteOptions(question,op1,op2):
    pen.clear()
    pen.goto(0,200)
    pen.write(question,False,"center",("Arial", 20, "bold"))
    pen.goto(-200,-150)
    pen.write(op1,False,"center",("Arial", 20, "bold"))
    pen.goto(200,-150)
    pen.write(op2,False,"center",("Arial", 20, "bold"))

def encode_decode():
    global stopped2_electricboogaloo, cypherbet, userkey, textstring, theUpper_case, result
    stopped2_electricboogaloo = True
    pen.clear()
    for letter in allLetters:
        wn.onkeypress(donothingdawg,letter)
    wn.listen()
    if isCaesar:
        cypherbet = caesarShift(userkey)
    else:
        cypherbet = monoAlphabet(userkey)
    theUpper_case = getCase(textstring)
    if isEncoding:
        encode(textstring,cypherbet,theUpper_case)
    else:
        decode(textstring,cypherbet,theUpper_case)
    pen.clear()
    pen.goto(0,0)
    pen.write(f"{typetxt.get(isCaesar)} {modetxt.get(isEncoding)}d text:\n{result}",False,"center",("Arial", 20, "bold"))
    with open ("assets/code/output.txt","w") as file1:
        file1.write(result)
    pen.goto(0,-200)
    pen.write(f"Text saved to\nassets/code/output.txt",False,"center",("Arial", 18, "normal"))
    pen.goto(-300,300)
    pen.write(f"press ESC to exit",font=("Arial", 12, "italic"))
    wn.onkeypress(byebye,"Escape")
    wn.listen()
    
def enterUserKey(let):
    global userinput, userkey, isCaesar, stopped2_electricboogaloo
    alttext = False
    pen.clear()
    if not stopped2_electricboogaloo:
        if let == "Return":
            try:
                int(userinput)
                if isCaesar:
                    userkey = int(userinput)
                    encode_decode()
                else:
                    alttext = True
                    userinput = ""
            except:
                if not isCaesar and monoReqs(userinput):
                    userkey = userinput
                    encode_decode()
                else:
                    alttext = True
                    userinput = ""

        elif let == "BackSpace":
            userinput = userinput[:-1]
        else:
            userinput += let
    if not stopped2_electricboogaloo:
        if not alttext:
            pen.goto(0,200)
            pen.write(f"Enter your {typetxt.get(isCaesar)} key:\nPress Enter to Finish",False,"center",("Arial", 20, "bold"))
            pen.goto(0,150)
            if userinput == "":
                pen.write("Type here:",False,"center",("Arial", 12, "italic"))
            else:
                pen.write(userinput,False,"center",("Arial", 15, "normal"))
        else:
            pen.goto(0,200)
            pen.write(f"Invalid Key. Try again.",False,"center",("Arial", 20, "bold"))
            pen.goto(0,150)
            pen.write("Type here:",False,"center",("Arial", 12, "italic"))
    alttext = False
    wn.listen()

def triggerKeyInput():
    global stopped, userinput
    userinput = ""
    stopped = True
    pen.clear()
    pen.goto(0,200)
    pen.write(f"Enter your {typetxt.get(isCaesar)} key:\nPress Enter to Finish",False,"center",("Arial", 20, "bold"))
    pen.goto(0,150)
    pen.write("Type here:",False,"center",("Arial", 12, "italic"))
    alphabet2 = alphabet + ["Return","BackSpace"] + numbers
    for letter in alphabet2:
        wn.onkeypress(lambda let=letter:enterUserKey(let),letter)
    wn.listen()

def enterUsertext(let):
    global userinput, isCaesar, stopped, textstring
    if not stopped and not let in lettersBlacklist:
        pen.clear()
        if let == "Return":
            try: # if file
                with open(userinput,"r") as file1:
                    for line in file1:
                        textstring = line
                        break
            except: # if text
                textstring = userinput
            stopped = True
            triggerKeyInput()
        elif let == "BackSpace":
            userinput = userinput[:-1]
        elif let == "space":
            userinput += " "
        else:
            userinput += let
        if not stopped:
            pen.goto(0,200)
            pen.write(f"Enter text to {modetxt.get(isEncoding)}:\nPress Enter to Finish",False,"center",("Arial", 20, "bold"))
            pen.goto(0,150)
            if userinput == "":
                pen.write("Type here:",False,"center",("Arial", 12, "italic"))
            else:
                pen.write(userinput,False,"center",("Arial", 15, "normal"))
            wn.listen()

def enablekeyboard():
    bt1.hideturtle()
    bt2.hideturtle()
    pen.clear()
    pen.goto(0,200)
    pen.write(f"Enter text to {modetxt.get(isEncoding)}:\nPress Enter to Finish",False,"center",("Arial", 20, "bold"))
    pen.goto(0,150)
    pen.write("Type here:",False,"center",("Arial", 12, "italic"))
    for letter in allLetters:
        wn.onkeypress(lambda let=letter:enterUsertext(let),letter)
    wn.listen()

def triggerCaeser(x,y):
    global isCaesar
    isCaesar = True
    enablekeyboard()

def triggerMono(x,y):
    global isCaesar
    isCaesar = False
    enablekeyboard()

def triggerEncode(x,y):
    global isEncoding
    isEncoding = True
    bt1.onclick(triggerCaeser)
    bt2.onclick(triggerMono)
    penWriteOptions(f"Select Encoding method",f"Click for\nCaesar",f"Click for\nMonoalphabetic")

def triggerDecode(x,y):
    global isEncoding
    isEncoding = False
    bt1.onclick(triggerCaeser)
    bt2.onclick(triggerMono)
    penWriteOptions(f"Select Decoding method",f"Click for\nCaesar",f"Click for\nMonoalphabetic")

# main ...........................
    
bt1.penup()
bt1.speed(0)
bt1.shapesize(7)
bt1.goto(-200,0)

bt2.penup()
bt2.speed(0)
bt2.shapesize(7)
bt2.goto(200,0)

pen.penup()
pen.speed(0)
pen.hideturtle()
penWriteOptions(f"Encode or Decode?",f"Click to\nEncode",f"Click to\nDecode")

bt1.onclick(triggerEncode)
bt2.onclick(triggerDecode)

wn.mainloop()
