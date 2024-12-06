import math as math
import numbers
if True: #This is just so i can hide the map from the edtor
    map = [['S', 'W'], ['N', 'S'], ['S', 'E'], ['N', 'S', 'E', 'W', 'A'], ['N', 'S', 'W'], ['S'], ['N', 'S'], ['S'], ['N', 'S'], ['N', 'S', 'E'], ['S', 'W'], ['S'], ['S', 'E'], ['N', 'S', 'E', 'A', 'W'], ['S', 'E', 'W'], ['S', 'W'], ['S', 'E'], ['S', 'E', 'W'], ['S', 'W'], ['N', 'S', 'E'], ['W', 'E'], ['N', 'W', 'S'], ['N'], ['S', 'E'], ['E', 'W', 'N', 'A', 'S'], ['N', 'W'], ['S', 'N'], [], ['S', 'E'], ['S', 'E', 'W'], ['N', 'W'], ['N'], [], ['S', 'E'], ['W', 'N'], ['E'], ['W', 'E'], ['N', 'W'], [], ['N', 'S'], ['N'], ['S', 'N'], ['S', 'E'], ['W'], ['S', 'E'], ['W', 'N', 'S'], ['S'], ['N'], [], ['N'], ['N', 'S', 'E'], ['S', 'E', 'W', 'A', 'N'], ['W'], ['N'], ['S'], ['N'], ['N', 'E'], ['S', 'W'], ['E'], ['W', 'S'], ['N', 'S'], ['S'], [], ['N'], [], ['N', 'S', 'E'], ['N', 'W'], ['S'], ['E'], ['E', 'S', 'W'], ['S', 'E', 'N', 'A', 'W'], ['S', 'W', 'N'], ['N'], ['N', 'S'], ['E'], ['N', 'W', 'S'], ['S'], [], ['N', 'E'], ['N', 'W'], ['S'], ['N'], ['N'], ['S', 'N', 'E'], ['W'], ['S'], ['N', 'S'], ['N', 'E'], ['W'], [], ['N', 'S'], ['S'], ['N', 'S'], ['N', 'S'], ['E'], ['S', 'W', 'N'], [], ['E'], ['W', 'S', 'E'], ['W', 'S', 'E'], ['E', 'W'], ['N', 'W', 'S'], ['S'], ['S'], ['N'], ['N'], ['S'], ['N', 'S'], ['E'], ['W'], ['E', 'N', 'S'], ['N', 'E', 'W'], ['E', 'W', 'S'], ['E', 'S', 'W'], ['N', 'W'], ['S', 'E'], ['N', 'W'], [], ['N'], ['N', 'E'], ['W'], ['N', 'S'], ['E'], ['W'], ['E', 'S'], ['S', 'N', 'W'], ['E'], ['W', 'S'], ['N'], ['N', 'E'], ['S', 'W'], ['S'], ['E'], ['W'], ['S'], [], ['S'], [], ['N', 'S'], ['N', 'S'], [], ['S'], [], ['N', 'E'], ['E', 'W'], ['S', 'W'], [], [], ['S', 'N'], ['E', 'S'], ['W'], [], ['N'], ['N', 'E'], ['N', 'W'], [], ['E'], ['W', 'N'], ['S'], ['S'], [], [], [], ['N', 'S', 'E'], ['W', 'N', 'E'], ['N', 'W'], ['N', 'E'], ['W', 'E'], ['S', 'W'], ['E'], ['N', 'W'], ['E', 'N'], ['S', 'W'], ['S'], ['N', 'S'], ['N'], ['N'], ['S'], ['E'], ['N', 'W'], ['E'], ['W', 'N'], ['N'], ['S'], ['S'], ['N', 'S'], ['S', 'E'], ['W'], ['N'], [], ['N', 'S', 'E'], ['S', 'W'], ['E'], ['E', 'W'], ['S', 'E', 'W'], ['S', 'E', 'W', 'A', 'N'], ['E', 'N', 'S', 'A', 'W'], ['W'], ['N'], ['S'], [], ['S'], ['S', 'E'], ['E', 'N', 'W'], ['N', 'W'], ['N', 'S'], ['N'], ['N', 'E'], ['W', 'N', 'S', 'A', 'E'], ['N', 'W', 'E'], ['W', 'S', 'E'], ['N', 'W'], ['E'], ['W'], ['N'], ['S'], ['S'], ['N'], ['S', 'N', 'E'], ['W', 'N'], ['E', 'N'], ['N', 'W'], ['N'], ['N', 'S'], ['S', 'E'], ['E', 'W', 'S'], ['S', 'W'], ['S'], ['N', 'S', 'E'], ['N', 'S', 'W'], [], ['S'], ['N', 'E'], ['W'], ['S', 'E'], ['E', 'W'], ['N', 'W'], ['S'], ['S', 'E'], ['S', 'W'], ['N', 'S', 'E'], ['W', 'S'], ['S', 'E'], ['S', 'W', 'N', 'A', 'E'], ['W'], ['N', 'E'], ['W'], [], ['S', 'E'], ['S', 'W', 'E'], ['W', 'E'], ['N', 'W'], ['N', 'S'], ['E'], ['N', 'W'], [], ['S', 'N'], [], [], ['N'], ['N', 'E', 'S'], ['W', 'N'], [], ['N', 'S'], ['N', 'E'], ['W', 'N', 'S', 'A', 'E'], ['W', 'N', 'E'], ['W'], ['N'], ['N', 'E'], ['W', 'E'], ['N', 'W', 'S'], ['S'], ['N', 'E'], ['W', 'S'], ['N', 'E'], ['S', 'W'], ['N', 'E'], ['W'], ['S', 'E'], ['W', 'S'], ['N', 'S'], ['N', 'E'], ['N', 'W', 'S'], ['S', 'E'], ['S', 'E', 'W'], ['S', 'E', 'W'], ['E', 'W'], ['N', 'S', 'E', 'A', 'W'], ['S', 'E', 'W'], ['E', 'W'], ['N', 'S', 'W'], ['N', 'E'], ['N', 'W', 'S'], ['E'], ['E', 'W', 'S'], ['W'], ['S'], ['E'], ['N', 'E', 'W'], ['W'], ['S', 'E'], ['N', 'W', 'S', 'A', 'E'], ['W', 'S'], [], ['E'], ['W'], ['E'], ['S', 'W'], ['N'], ['N', 'E'], ['N', 'S', 'W', 'A', 'E'], ['S', 'W'], ['N', 'S'], ['E'], ['W'], ['E', 'N'], ['E', 'W'], ['N', 'W'], ['N', 'S'], ['N', 'E'], ['N', 'W'], ['N', 'S'], ['N'], [], ['N', 'E'], ['W'], ['N'], ['N', 'E'], ['S', 'E', 'W'], ['S', 'W'], ['N', 'S'], [], ['S'], ['N'], [], ['S'], [], ['S', 'N', 'E'], ['N', 'W', 'S'], ['S'], ['N', 'S', 'E'], ['W', 'S'], ['S'], ['E'], ['W', 'S'], ['N'], ['S'], ['N', 'S'], [], ['N', 'E'], ['S', 'E', 'W'], ['W'], [], ['N', 'S', 'E'], ['E', 'N', 'W'], ['E', 'N', 'W'], ['E', 'W'], ['S', 'W', 'N'], ['S'], ['N'], ['N', 'S'], [], ['E'], ['N', 'W'], ['E'], ['S', 'E', 'W'], ['E', 'W'], ['S', 'E', 'W'], ['W'], ['S', 'E'], ['W'], ['E'], ['W'], ['S'], ['S'], ['S'], ['N'], ['N', 'S', 'E'], ['E', 'W'], ['N', 'S', 'W'], ['N', 'S'], ['N', 'E'], ['W', 'N'], ['N', 'S'], ['N'], ['N'], ['N'], ['N'], ['N'], ['N', 'E'], ['N', 'W', 'E'], ['N', 'W', 'E'], ['N', 'W'], ['N', 'E'], ['N', 'W'], ['N'], ['NS'], ['N', 'S'], ['N', 'E']]

sendInCommands = ["F","B","L","R","SCN","RUN"]
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

def turnPlayer(direction):
    if direction == "R":
        Facing = (Facing + 1) % 4
    elif direction == "L":
        Facing = (Facing - 1) % 4

# Innitialize
mapLength = int(math.sqrt(len(map)))
movements = {
    0: mapLength,
    1: -mapLength,
    2: -1,
    3: 1}
jumpCheckers = {
    "JMP": lambda: True,
    "JEZ": lambda: (plrVariable == 0),
    "JNZ": lambda: (plrVariable != 0),
    "JAV": lambda: True}
directionDefs = {
    0: "N",
    1: "E",
    2: "S",
    3: "W"}
plrList = []

while True: # Game Loop
    dummy = ""
    # Get Inputs
    while "RUN" not in plrList:
        try:
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
        except Exception:
            print("Invalid Format. Insert Commands as cmd(x)")
    # Run
    plrList = plrList[0:-1]
    updateCmdBoard()
    # Start Loops
    LoopCount = 0
    index = 0
    Position = 200
    plrVariable = 0
    Facing = 0
    TurnReporter = []
    while index < len(plrList): 
        cmd = plrList[index]
        index += 1
        # Movment
        if cmd in ["L","R"]:
            turnPlayer(cmd)
        elif cmd == "F":
            if directionDefs.get(Facing) not in map[Position]:
                Position += movements.get(Facing,0)
            else:
                TurnReporter = ["Crashed"]
                break
        elif cmd == "B":
            if directionDefs.get((Facing+2)%4) not in map[Position]:
                Position += movements.get((Facing+2)%4,0)
            else:
                TurnReporter = ["Crashed"]
                break
        elif cmd == "SCN":
            TurnReporter.append(map[Position])
        # Jump/Var Detection and var Commands  
        # This formats the command  
        if cmd[0:3] in jumpValCommands:
            runval = int(cmd[4:-1])
            cmd = cmd[0:3]
        # Commands
        if cmd == "VAL":
            plrVariable = runval
        elif cmd == "VMD":
            plrVariable += runval
        # Jump Commands
        elif jumpCheckers.get(cmd,lambda:False)():
            LoopCount += 1
            index = runval
            if cmd == "JAV":
                plrVariable += 1
        if LoopCount>256:
            TurnReporter = ["Infinite Loop"]
            break

    TurnReporter.append("Complete")
    for i in TurnReporter: print(i)
    if input("Continue? (y/n): ") == "n": break
    updateCmdBoard()
