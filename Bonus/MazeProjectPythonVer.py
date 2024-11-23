import numbers
map = [["S","W"],["S"],["S"],["N"],["B"],["B"],["N","S","E","W"],["N","W"],["N","E"]]

sendInCommands = ["F","R","L","B","SCN","RUN"]
Commands = ["CLR","DEL","MOD"]
jumpValCommands = ["VAL","VMD","JMP","JEZ","JNZ","JAV"]


plrList = []
dummy = ""

while "RUN" not in plrList:
    try:
        dummy = input("Enter Input: ")
        dummy = dummy.upper()
        # Send-ins
        if dummy in sendInCommands:
            plrList.append(dummy)
        # Editing Commands
        elif dummy[0:3] in Commands:
            if dummy == "CLR":
                plrList = []
            elif dummy == "DEL":
                plrList = plrList[0:-1]
            elif dummy[0:3] == "MOD":
                commandval = int(dummy[4:-1])
                if isinstance(commandval, numbers.Number):
                    plrList.insert(commandval,input(f"Replace Line {commandval} ({plrList.pop(commandval)}) with: "))
        # Jump and Values
        elif dummy[0:3] in jumpValCommands:
            print("Finish this later")
        
        
        
        print("Commands:")
        for i in range(len(plrList)):
            print(f"{i}. {plrList[i]}")
    except:
        print("Invalid Syntax")
        

plrList = plrList[0:-1]
print("Done")
print(plrList)
