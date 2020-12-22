IN = [x for x in open("day22.txt", "r").read().splitlines()]

decks = []


def init():
    global decks

    id = ""
    curr = []
    for line in IN:
        if "Player" in line:
            id = int(line.replace("Player ", "").replace(":", ""))
        elif line == "":
            decks.append(curr)
            curr = []
        else:
            curr.append(int(line))
    decks.append(curr)
    curr = []


def playRound():
    deckP1, deckP2 = decks
    if len(deckP1) == 0 or len(deckP2) == 0:
        return True
    p1Card = deckP1[0]
    deckP1.pop(0)
    p2Card = deckP2[0]
    deckP2.pop(0)

    if p1Card > p2Card:
        deckP1.append(p1Card)
        deckP1.append(p2Card)
    elif p1Card < p2Card:
        deckP2.append(p2Card)
        deckP2.append(p1Card)
    else:
        print("DRAW ??!")
    return False


def getAns(arr):
    sum = 0
    size = len(arr)
    for i in range(1, size + 1):
        sum += (i) * arr[-i]
    return sum


init()
r = 0
while not playRound():
    r += 1
    print("Round " + str(r))
    print(decks)

if len(decks[0]) == 0:
    print(getAns(decks[1]))
else:
    print(getAns(decks[0]))
#18 min