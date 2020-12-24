IN = [line for line in open("day24.txt", "r").read().splitlines()]

SIZE = 240

#False = white
#True = Black
grid = [[False for y in range(SIZE)] for x in range(SIZE)]

refX = int(SIZE / 2)
refY = int(SIZE / 2)

dire = ["e", "se", "sw", "w", "nw", "ne"]


def draw():
    s = ""
    for y in range(SIZE):
        if y % 2 != 0:
            s += " "
        for x in range(SIZE):
            if y == refY and x == refX:
                s += ("O" if not grid[y][x] else "X") + " "
            else:
                s += ("." if not grid[y][x] else "#") + " "
        s += "\n"
    print(s)


def flip(cx, cy, line):
    s = ""
    if line == "":
        grid[cy][cx] = not grid[cy][cx]
        return
    for char in line:
        s += char
        if s in dire:
            if s == "e":
                flip(cx + 1, cy, line[len(s):])
            elif s == "se":
                if cy % 2 != 0:
                    flip(cx + 1, cy + 1, line[len(s):])
                else:
                    flip(cx, cy + 1, line[len(s):])
            elif s == "sw":
                if cy % 2 != 0:
                    flip(cx, cy + 1, line[len(s):])
                else:
                    flip(cx - 1, cy + 1, line[len(s):])
            elif s == "w":
                flip(cx - 1, cy, line[len(s):])
            elif s == "nw":
                if cy % 2 != 0:
                    flip(cx, cy - 1, line[len(s):])
                else:
                    flip(cx - 1, cy - 1, line[len(s):])
            elif s == "ne":
                if cy % 2 != 0:
                    flip(cx + 1, cy - 1, line[len(s):])
                else:
                    flip(cx, cy - 1, line[len(s):])
            s = ""
            return
        else:
            continue


def count():
    summ = 0
    for line in grid:
        for x in line:
            if x:
                summ += 1
    return summ


for line in IN:
    flip(refX, refY, line)
draw()
print(str(count()))

#30 min