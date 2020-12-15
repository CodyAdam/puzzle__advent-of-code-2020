IN = open("day15.txt", "r").read().split(",")

liste = dict()

for i in range(len(IN)):
    liste[int(IN[i])] = i+1

turn = 3
current = 6


def count(key):
    if liste[key] == turn-1:
        liste[key] = turn
        return 0
    else:
        tmp = liste[key]
        liste[key] = turn
        return turn - tmp


while turn < 10:
    print(liste)
    print(current)
    current = count(current)
    turn += 1
# 34min
