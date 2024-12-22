possiblewords = open("files/wordle-nyt-words-14855.txt", "r").readlines()
possiblewords = [word.strip() for word in possiblewords]
possiblewords2 = possiblewords.copy()
unusedchars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("\nenter the letter in lowercase then its position")
print("e.g. if f is the fifth letter put in f5")
print("for grays, just put in the letter")
print("to move on to the next category, enter continue")
print("\n------------------\n")

greens = []
while True:
    green = input("enter greens: ")
    if green == "continue":
        break
    elif len(green) != 2 or not green.isalnum():
        print("enter in the proper format")
    else:
        greens.append([green[0], int(green[1])])

temp = []
if greens:
    for letter, position in greens:
        try:
            unusedchars.remove(letter)
        except:
            pass
        for word in possiblewords:
            if word[position-1] == letter:
                temp.append(word)
        possiblewords = temp.copy()
        temp = []

print("\n------------------\n")

yellows = []
while True:
    yellow = input("enter yellows: ")
    if yellow == "continue":
        break
    elif len(yellow) != 2 or not green.isalnum():
        print("enter in the proper format")
    else:
        yellows.append([yellow[0], int(yellow[1])])

if yellows:
    for letter, position in yellows:
        try:
            unusedchars.remove(letter)
        except:
            pass
        for word in possiblewords:
            if (letter in word) and (word[position-1] != letter):
                temp.append(word)
        possiblewords = temp.copy()
        temp = []

print("\n------------------\n")

grays = []
while True:
    gray = input("enter grays: ")
    if gray == "continue":
        break
    elif len(gray) != 1 or not gray.isalnum():
        print("enter in the proper format")
    else:
        grays.append(gray)

if grays:
    for letter in grays:
        try:
            unusedchars.remove(letter)
        except:
            pass
        for word in possiblewords:
            if letter not in word:
                temp.append(word)
        possiblewords = temp.copy()
        temp = []

print("\n------------------\n")

print("possible word(s) are:")
if possiblewords: 
    for word in possiblewords: print(word)
else: print("none")


if len(possiblewords) > 3 and len(unusedchars) > 3:
    print("\n------------------\n")

    goodwords = []
    for word in possiblewords2:
        charcount = 0
        for char in unusedchars:
            if char in word:
                charcount += 1
        if charcount > 3:
            goodwords.append([word, charcount])

    print("possible characters are: " + ", ".join(unusedchars))
    print("goodwords would be:")
    if goodwords:
        goodwords.sort(key=lambda x: x[1], reverse=True)
        if len(goodwords) > 10:
            for word, chars in goodwords[:11]: print(word + "(" + str(chars) + ")")
        else:
            for word, chars in goodwords: print(word + "(" + str(chars) + ")")
    else: print("none")