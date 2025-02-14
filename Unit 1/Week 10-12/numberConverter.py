import turtle as trtl
pen = trtl.Turtle()
wn = trtl.Screen()

btrtl = []
for i in range(6):
    temp = trtl.Turtle(shape="circle")
    temp.speed(0)
    temp.shapesize(8)
    temp.penup()
    btrtl.append(temp)

hexdec = {"a": 10,
          "b": 11,
          "c": 12,
          "d": 13,
          "e": 14,
          "f": 15}
dechex = {10: "a",
          11: "b",
          12: "c",
          13: "d",
          14: "e",
          15: "f"}





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


def getInput(question,cond,Inputs=[]):
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
    for letter in Inputs:
        wn.onkeypress(None,letter)
    wn.listen()
    pen.clear()
    return answer


def hidebuttons():
    pen.clear()
    for button in btrtl:
        button.clear()
        button.onclick(None)
        button.hideturtle()


def bt1(x,y): # 2 - 10
    hidebuttons()
    number = getInput(f"Enter number in Binary",[],["1","0","BackSpace","Return"])
    total = convertToDecimal(number,2)
    print(total)


def bt2(x,y): # 10 - 16
    hidebuttons()
    number = getInput(f"Enter number in Hexadecimal",[],["0","1","2","3","4","5","6","7","8","9",
                                                             "a","b","c","d","e","f","BackSpace","Return"])
    dec = convertToDecimal(number,16)
    total = convertToBinary(dec)
    print(total)

def bt3(x,y): # 16 - 2
    hidebuttons()

def bt4(x,y): # 10 - 2
    hidebuttons()
    number = getInput(f"Enter number in Decimal",[],["0","1","2","3","4","5","6","7","8","9","BackSpace","Return"])
    total = convertToBinary(number)
    print(total)

def bt5(x,y): # 16 - 10
    hidebuttons()
    number = getInput(f"Enter number in Hexadecimal",[],["0","1","2","3","4","5","6","7","8","9",
                                                             "a","b","c","d","e","f","BackSpace","Return"])
    total = convertToDecimal(number,16)
    print(total)

def bt6(x,y): # 2 - 16
    hidebuttons()
    print(6)

def convertToDecimal(number,base):
    number = str(number)
    numlist = []
    for char in number:
        if char in ["a","b","c","d","e","f"]:
            numlist.append(hexdec.get(char))
        else:
            numlist.append(int(char))
    numlist.reverse()
    total = 0
    for i in range(len(numlist)):
        total += numlist[i]*(base**i)
    return total

def convertToBinary(dec):
    dec = int(dec)
    highest = 1
    baselist = [1]
    while dec >= highest and dec != 0:
        highest *= 2
        baselist.append(highest)
    val = dec
    baselist.reverse()
    print(baselist)
    for i in range(len(baselist)):
        if val >= baselist[i]:
            val -= baselist[i]
            baselist[i] = "1"
        else:
            baselist[i] = "0"
    print(baselist)
    total = ""
    for num in baselist:
        total += num
    total = int(total)
    return total
        
def convertToHex(bas2):
    bas2 = str(bas2)
    numlist = []
    for char in bas2:
        numlist.append(int(char))
    while len(numlist) % 4 != 0:
        numlist.append(0)
    numlist.reverse()
    numlist2 = []
    for i in range(0,len(numlist),4):
        val = ""
        for num in numlist[i:i+3]:
            val += num
        val = int(val)
        val = convertToDecimal(val,2)
        numlist2.append(val)
    





pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write(f"Select Conversion",False,"center",("Arial", 20, "bold"))
texts = ["Binary to Decimal","Decimal to Hexadecimal","Hexadecimal to Binary","Decimal to Binary","Hexadecimal to Decimal","Binary to Hexadecimal"]
location = [(-300,150),(0,150),(300,150),(-300,-150),(0,-150),(300,-150)]
procedures = [bt1,bt2,bt3,bt4,bt5,bt6]
for i in range(6):
    btrtl[i].goto(location[i])
    btrtl[i].sety(btrtl[i].ycor()-120)
    btrtl[i].write(texts[i],False,"center",("Arial", 15, "normal"))
    btrtl[i].goto(location[i])
    btrtl[i].onclick(procedures[i])


wn.mainloop()
