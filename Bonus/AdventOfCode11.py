
RockPusher = ["5", "127", "680267", "39260", "0", "26", "3553", "5851995"]
for loop in range(25):
    print(loop)
    SchrodingersRockPile = []
    for i in RockPusher:
        if i == "0":
            SchrodingersRockPile.append("1")
        elif len(i)%2 == 0:
            half = len(i)//2
            add1 = i[0:half]
            add2 = str(int(i[half:])*1)
            SchrodingersRockPile.append(add1)
            SchrodingersRockPile.append(add2)
        else:
            addelse = str(int(i)*2024)
            SchrodingersRockPile.append(addelse)
    RockPusher = SchrodingersRockPile
    SchrodingersRockPile = []


TellSchrodinger___iLived = len(RockPusher)
print(TellSchrodinger___iLived)
