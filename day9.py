IN = [int(x) for x in open("day9.txt", "r").read().splitlines()]

preamble = []
size = 25


def isSum(x):
    for a in preamble:
        for b in preamble:
            if (a + b == x and a != b):
                return True
    return False


for i in range(len(IN)):
    if (i < size):
        preamble.append(IN[i])
        print(IN[i])
        continue
    if (not isSum(IN[i])):
        print(str(IN[i]) + " PAS UNE SOMME")
    if (i + 1 < len(IN)):
        preamble.pop(0)
        preamble.append(IN[i])
    else:
        print("END OF THE LINE")
#9 min