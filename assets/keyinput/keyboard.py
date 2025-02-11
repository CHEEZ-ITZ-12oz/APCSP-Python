import turtle as trtl
pen = trtl.Turtle()
wn = trtl.Screen()




def enterUserText(let,message,valids):
    global stopped, answer, userinput
    alttext = False
    pen.clear()
    let = str(let)
    if not stopped:
        if let == "Return":
                if userinput in valids: # edit condition
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
    pen.clear()
    return answer
