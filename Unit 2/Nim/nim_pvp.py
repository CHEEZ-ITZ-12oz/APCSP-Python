rocks = 20
player1 = True

while True:
    if player1: print("Player 1")
    else: print("Player 2")
    print(f"There are {rocks} rocks. Select 1, 2, or 3 to remove.")
    while True:
        try:
            pull = int(input(""))
            if pull > 0 and pull <= 3:
                break
        except:
            print("Invalid Input. Try again.")
    rocks -= pull
    player1 = not(player1)
    if rocks <= 0:
        break
    
if player1: print("Player 1 Wins!")
else: print("Player 2 Wins!")

