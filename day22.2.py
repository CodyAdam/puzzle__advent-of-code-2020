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


def playGame(decks):
    history = []

    deckP1, deckP2 = decks.copy()
    while len(deckP1) != 0 and len(deckP2) != 0:

        # print('Decks : ')
        # print(deckP1)
        # print(deckP2)

        if (deckP1, deckP2) in history:
            return 1
        history.append((deckP1.copy(), deckP2.copy()))

        p1Card = deckP1[0]
        deckP1.pop(0)
        p2Card = deckP2[0]
        deckP2.pop(0)

        combatWinner = 0
        if len(deckP1) >= p1Card and len(deckP2) >= p2Card:
            # print("---- SARTING A SUB COMBAT ---- ")
            combatWinner = playGame([deckP1[:p1Card], deckP2[:p2Card]])

        if combatWinner == 1 or (combatWinner == 0 and p1Card > p2Card):
            deckP1.append(p1Card)
            deckP1.append(p2Card)
        elif combatWinner == 2 or (combatWinner == 0 and p1Card < p2Card):
            deckP2.append(p2Card)
            deckP2.append(p1Card)
        else:
            print("DRAW ??!")
    if len(deckP1) == 0:
        # print("---- ENDING ---- winner : P2")
        return 2
    else:
        # print("---- ENDING ---- winner : P1")
        return 1


def getAns(arr):
    sum = 0
    size = len(arr)
    for i in range(1, size + 1):
        sum += (i) * arr[-i]
    return sum


init()
if (playGame(decks) == 2):
    print(getAns(decks[1]))
else:
    print(getAns(decks[0]))
#18 min