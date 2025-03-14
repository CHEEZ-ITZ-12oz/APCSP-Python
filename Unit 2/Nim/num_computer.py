import random

rocks = 20
player1 = True

while True:
    if player1: 
        print("Player 1")
        print(f"There are {rocks} rocks. Select 1, 2, or 3 to remove.")
        while True:
            try:
                pull = int(input(""))
                if pull > 0 and pull <= 3:
                    break
            except:
                print("Invalid Input. Try again.")
    else: 
        if rocks % 4 == 0: pull = 3
        elif rocks % 4 == 1: pull = 2
        elif rocks % 4 == 2: pull = 1
        else: pull = random.randint(1,3)
        print(f"Computer\nThere are {rocks} rocks. Select 1, 2, or 3 to remove.")
        print(pull)
   
    rocks -= pull
    player1 = not(player1)
    if rocks <= 0:
        break
    
if player1: print("Player 1 Wins!")
else: print("Computer Wins!")







