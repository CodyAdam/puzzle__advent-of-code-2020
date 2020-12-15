IN = [x for x in open("day5.txt", "r").read().splitlines()]


def dicho(inter, str):
    min = inter[0]
    max = inter[len(inter) - 1]
    if (min == max): return max

    letter, rest = str[0], str[1:]

    if (letter == "F" or letter == "L"):
        inter = range(min, int(max + 1 - (max - min) / 2))
    elif (letter == "B" or letter == "R"):
        inter = range(int(min + 1 + (max - min) / 2), 1 + max)
    else:
        print("letter not found ??? !>")

    return dicho(inter, rest)


def id(str):
    return dicho(range(0, 128), str) * 8 + dicho(range(0, 8), str[7:])


max = 0
for line in IN:
    cur = id(line)
    if (max < cur):
        max = cur
print(max)
#25 min