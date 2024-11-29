import math as math
import numbers
map = [["S","W"],["S"],["S"],["N"],[],["E"],["N","S","E","W"],["N","W"],["N","E"]]

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

# Innitialize
mapLength = int(math.sqrt(len(map)))
movements = {
    "F": mapLength,
    "B": -mapLength,
    "L": -1,
    "R": 1}
collisionCheck = {
    "F": "N",
    "B": "S",
    "L": "W",
    "R": "E"}
jumpCheckers = {
    "JMP": lambda: True,
    "JEZ": lambda: (plrVariable == 0),
    "JNZ": lambda: (plrVariable != 0),
    "JAV": lambda: True}
plrList = []

while True: # Game Loop
    dummy = ""
    while "RUN" not in plrList:
        dummy = input("Enter Input: ")
        dummy = dummy.upper()
        # Editing
        if dummy[0:3] in Commands:
            if dummy == "CLR":
                plrList = []
                updateCmdBoard()
            elif dummy == "DEL":
                plrList = plrList[0:-1]
                updateCmdBoard()
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
    # Run
    plrList = plrList[0:-1]
    updateCmdBoard()
    # Start Loops
    LoopCount = 0
    index = 0
    Position = 0
    plrVariable = 0
    TurnReporter = []
    while index < len(plrList): 
        cmd = plrList[index]
        index += 1
        # Movment
        if collisionCheck.get(cmd,"Zeta!!!!") not in map[Position]:
            Position += movements.get(cmd,0)
        elif movements.get(cmd,0) != 0:
            TurnReporter = ["Crashed"]
            break
        if cmd == "SCN":
            TurnReporter.append(map[Position])
        # Jump/Var Detection and var Commands    
        if cmd[0:3] in jumpValCommands:
            runval = int(cmd[4:-1])
            cmd = cmd[0:3]
        if cmd == "VAL":
            plrVariable = runval
        elif cmd == "VMD":
            plrVariable += runval
        # Jump Commands
        elif jumpCheckers.get(cmd,lambda: False)():
            LoopCount += 1
            index = runval
            if cmd == "JAV":
                plrVariable += 1
        if LoopCount>256:
            TurnReporter = ["Infinite Loop"]
            break

    TurnReporter.append("Complete")
    for i in TurnReporter: print(i)
    if input("Type Anything to Continue: ") == "exit": break
    updateCmdBoard()
