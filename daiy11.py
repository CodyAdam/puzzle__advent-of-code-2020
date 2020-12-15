IN = [[y for y in x] for x in open("day11.txt", "r").read().splitlines()]

TMP = [[str(x + "") for x in y] for y in IN]


def occupied(x, y):
    sum = 0

    for j in range(y - 1 if y - 1 >= 0 else y,
                   y + 2 if y + 2 <= len(IN) else y + 1):
        for i in range(x - 1 if x - 1 >= 0 else x,
                       x + 2 if x + 2 <= len(IN[0]) else x + 1):
            if (IN[j][i] == "#" and (y != j or x != i)):
                sum += 1
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
                if occupied(i, j) >= 4:
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
    draw(IN)
    lastSeat = seat
    print("step2")
    seat = step2()
    IN = TMP
    TMP = [[str(x + "") for x in y] for y in IN]
    draw(IN)
draw(IN)
print(seat)
#1h42min