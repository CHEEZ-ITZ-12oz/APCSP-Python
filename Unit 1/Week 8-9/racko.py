import random
# setup ...........
deck = list(range(1, 61))
random.shuffle(deck)
# functions ............

def instructions():
    print()
    print('The goal of the game is to get the cards in your rack of cards')
    print('into ascending order. Your rack has ten slots numbered 1 to 10.')
    print('During your turn you can draw the top card of the deck or take')
    print('the top card of the discard pile.')
    print('If you draw the top card of the deck, you can use that card to')
    print('replace a card in one slot of your rack. The replaced card goes to')
    print('the discard pile.')
    print('Alternatively you can simply choose to discard the drawn card.')
    print('If you take the top card of the discard pile you must use it to')
    print('replace a card in one slot of your rack. The replaced card goes')
    print('to the top of the discard pile.')

def infoPrint(plr1):
    print()
    if plr1: 
        print("Player 1's Turn:")
        print(f"> Current rack: {rack1}")
    else:
        print("Player 2's Turn:")
        print(f"> Current rack: {rack2}")
    print(f"Top of Discard Pile: {discard[0]}")

def getRack(rSize):
    global deck
    listicle = []
    for i in range(rSize):
        insert = deck.pop(0)
        listicle.append(insert)
    while wincheck(listicle):
        random.shuffle(listicle)
    return(listicle)

def checkIsDeckDepleated():
    global deck, discard
    if len(deck) < 2:
        discardSave = discard.pop(0)
        deck += random.shuffle(discard)
        discard = [discardSave]

def cardInsert(card,plr1):
    global rack1, rack2, discard
    print()
    while True:
        try:
            choice = int(input(f"Enter number to replace with {card}: "))
            if plr1 and choice in rack1:
                idx = rack1.index(choice)
                discard.insert(0,rack1[idx])
                rack1[idx] = card
                print()
                print(f"> Your new rack is: {rack1}")
                break
            elif not plr1 and choice in rack2:
                idx = rack2.index(choice)
                discard.insert(0,rack2[idx])
                rack2[idx] = card
                print()
                print(f"> Your new rack is: {rack2}")
                break
            print(f"{choice} is not in your rack.")
        except:
            print(f"Invalid Input. Try again.")

def turn(plr):
    global deck, discard
    checkIsDeckDepleated()
    choice = input(f"Enter 'd' to draw from the Deck. Enter anything else to draw from Discard: ")
    if choice == "d":
        card = deck.pop(0)
        print()
        print(f"Drawn Card: {card}")
        choice = input(f"Enter 'k' to keep card. Enter anything else to discard: ")
        if choice == "k":
            cardInsert(card,plr)
        else:
            discard.insert(0,card)
    else:
        card = discard.pop(0)
        cardInsert(card,plr)

def wincheck(rack):
    rackCheck = rack[::1]
    rackCheck.sort()
    if rack == rackCheck:
        return True
    else:
        return False


# main .............
"""
if input("Display instructions? (y/n): ") == "y":
    instructions()
print()
"""
while True:
    try:
        rSize = int(input('Enter the size of the rack. (Between 5 and 10): '))
        if 5 <= rSize <= 10:
            break
        print(rSize, 'is not a valid rack size.')
    except:
        ("Not a valid input")  
print()

rack1 = getRack(rSize)
rack2 = getRack(rSize)
discard = [deck.pop(0)]
IsPlr1 = True


while True:
    infoPrint(IsPlr1)
    turn(IsPlr1)
    if wincheck(rack1):
        print()
        print("Player 1 Wins!")
        break
    infoPrint(not IsPlr1)
    turn(not IsPlr1)
    if wincheck(rack2):
        print()
        print("Player 2 Wins!")
        break
print()

