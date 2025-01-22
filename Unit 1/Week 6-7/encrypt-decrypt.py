# setup
import string


alphabet = list(string.ascii_lowercase)
cypherbet = []
theUpper_case = []
result = ""
# functions
modetxt = {True: "encode", False: "decode"}
typetxt = {True: "Caesar", False: "Monoalphabetic"}

def fixAlphabet():
    global alphabet
    alphabet = list(string.ascii_lowercase)

def caesarShift(value):
    shifted = alphabet
    for i in range(value):
        shifted.append(shifted.pop(0))
    fixAlphabet()
    return(shifted)
def monoAlphabet(key):
    monolist = list(key)
    reversedAlpha = alphabet[::-1]
    for letter in reversedAlpha:
        if not letter in monolist:
            monolist.append(letter)
    fixAlphabet()
    return(monolist)
def getCase(message):
    messageList = list(message)
    caselist = []
    for letter in messageList:
        if letter.isupper():
            caselist.append(True)
        else: caselist.append(False)
    return(caselist)
def monoReqs(key):
    keylist = list(key)
    for letter in keylist:
        if keylist.count(letter) > 1:
            return(False)
    return(True)
def encode(usertext,alpha,caseread):
    global result
    usertext = usertext.lower()
    usertext = list(usertext)
    endlist = []
    textreader = ""
    letterinsert = ""
    endtext = ""
    for i in range(len(usertext)):
        textreader = usertext[i]
        if textreader in alphabet:
            letterinsert = alpha[alphabet.index(textreader)]
        else:
            letterinsert = textreader
        endlist.append(letterinsert)
    for i in range(len(usertext)):
        textreader = endlist[i]
        if caseread[i]:
            endtext += textreader.upper()
        else:
            endtext += textreader
    result = endtext

def decode(usertext,alpha,caseread):
    global result
    usertext = usertext.lower()
    usertext = list(usertext)
    endlist = []
    textreader = ""
    letterinsert = ""
    endtext = ""
    for i in range(len(usertext)):
        textreader = usertext[i]
        if textreader in alphabet:
            letterinsert = alphabet[alpha.index(textreader)]
        else:
            letterinsert = textreader
        endlist.append(letterinsert)
    for i in range(len(usertext)):
        textreader = endlist[i]
        if caseread[i]:
            endtext += textreader.upper()
        else:
            endtext += textreader
    result = endtext
# main
while True: # Encode/Decode
    userinput = input(f"Encode (e) or Decode (d) ?: ")
    if userinput == "e": 
        isEncoding = True
        break
    elif userinput == "d":
        isEncoding = False
        break
while True: # Caesar/Monoalphabetic
    userinput = input(f"Which algorithm would you like to use to {modetxt.get(isEncoding)}? Caesar (c) or Monoalphabetic (m)?: ")
    if userinput == "c": 
        isCaesar = True
        break
    elif userinput == "m":
        isCaesar = False
        break
userinput = input(f"Enter text or enter filepath to {modetxt.get(isEncoding)}: ")
try: # if file
    with open(userinput,"r") as file1:
        for line in file1:
            textstring = line
            break
except: # if text
    textstring = userinput

print(textstring)

while True: # Get Key
    userinput = input(f"Enter your key: ")
    try:
        int(userinput)
        if isCaesar:
            userkey = int(userinput)
            break
    except:
        if not isCaesar and monoReqs(userinput):
            userkey = userinput
            break
    print("Not a valid key")


if isCaesar: cypherbet = caesarShift(userkey)
else: cypherbet = monoAlphabet(userkey)

theUpper_case = getCase(textstring)

if isEncoding: encode(textstring,cypherbet,theUpper_case)
else: decode(textstring,cypherbet,theUpper_case)

print(result)
