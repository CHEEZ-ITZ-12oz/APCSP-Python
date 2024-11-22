map = [["S","W"],["S"],["S"],["N"],["B"],["B"],["N","S","E","W"],["N","W"],["N","E"]]

sendInCommands = ["F","R","L","B","SCN","RUN"]
Commands = ["CLR","DEL","MOD"]

plrInput = True
plrList = []
dummy = ""

while "RUN" not in plrList:
    dummy = input("Enter Input: ")
    dummy = dummy.upper()
    # Send-ins
    if dummy in sendInCommands:
        plrList.append(dummy)
    #Commands
        dummy_c = dummy[0:2]
    elif dummy_c in Commands:
        if dummy_c == "CLR":
            plrList = []
        elif dummy_c == "DEL":
            plrList = plrList[0,-1]

plrList = plrList[0,-1]
print("Done")
print(plrList)
