IN = [[y for y in x] for x in open("day11.txt", "r").read().splitlines()]

TMP = [[str(x + "") for x in y] for y in IN]


def occupied(x, y):
    dir = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
           (-1, 1)]
    sum = 0
    for d in dir:
        ix, iy = d
        cx = x
        cy = y
        while (cx + ix in range(len(IN[0])) and cy + iy in range(len(IN))):
            cx += ix
            cy += iy
            if (IN[cy][cx] == "#"):
                sum += 1
                break
            elif (IN[cy][cx] == "L"):
                break
    return sum


def step1():
    for j in range(len(IN)):
        for i in range(len(IN[0])):
            if (occupied(i, j) == 0 and IN[j][i] == "L"):
                TMP[j][i] = "#"


def step2():
    sum = 0
    for j in range(len(IN)):
        for i in range(len(IN[0])):
            if (IN[j][i] == "#"):
                sum += 1
                if occupied(i, j) >= 5:
                    TMP[j][i] = "L"
    return sum


def draw(t):
    s = ""
    for x in t:
        for i in x:
            s += i
        s += "\n"
    print(s)


lastSeat = 0
seat = 1
while (seat != lastSeat):
    print("step1")
    step1()
    IN = TMP
    TMP = [[str(x + "") for x in y] for y in IN]
    lastSeat = seat
    print("step2")
    seat = step2()
    IN = TMP
    TMP = [[str(x + "") for x in y] for y in IN]
draw(IN)
print(seat)

#14 min