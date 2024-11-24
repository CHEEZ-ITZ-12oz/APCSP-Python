import numbers
map = [["S","W"],["S"],["S"],["N"],["B"],["B"],["N","S","E","W"],["N","W"],["N","E"]]

sendInCommands = ["F","R","L","B","SCN","RUN"]
Commands = ["CLR","DEL","MOD"]
jumpValCommands = ["VAL","VMD","JMP","JEZ","JNZ","JAV"]

def Isnumber(num):
    return isinstance(num, numbers.Number)

def updateCmdBoard():
    print("Commands:")
    for i in range(len(plrList)):
        print(f"{i}. {plrList[i]}")

def validCmd(cmd):
    if (cmd in sendInCommands) or (cmd[0:3] in jumpValCommands):
        return True
    else:
        return False

# Start
plrList = []
dummy = ""

while "RUN" not in plrList:
    try:
        dummy = input("Enter Input: ")
        dummy = dummy.upper()
        # Editing
        if dummy[0:3] in Commands:
            if dummy == "CLR":
                plrList = []
            elif dummy == "DEL":
                plrList = plrList[0:-1]
            elif dummy[0:3] == "MOD":
                commandval = int(dummy[4:-1])
                if Isnumber(commandval):
                    dummy = input(f"Replace Line {commandval} ({plrList[commandval]}) with: ")
                    dummy = dummy.upper()
                    if validCmd(dummy):
                        plrList[commandval]=dummy
                        updateCmdBoard()
                    else:
                        updateCmdBoard()
                        print("Invalid Input")
        elif validCmd(dummy):
            plrList.append(dummy)
            updateCmdBoard()
        else:
            updateCmdBoard()
            print("Invalid Input")
    except:
        print("Something Went Wrong")
        

plrList = plrList[0:-1]
print("Done")
print(plrList)
