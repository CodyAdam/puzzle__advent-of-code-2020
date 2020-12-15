IN = [x for x in open("day12.txt", "r").read().splitlines()]

OP = []
for i in range(len(IN)):
    OP.append([])
    OP[i].append(IN[i][0])
    OP[i].append(int(IN[i][1:]))

x = 0
y = 0
wx = 10
wy = 1

for op in OP:
    print(op)
    if op[0] == "N":
        wy += op[1]
    elif op[0] == "S":
        wy -= op[1]
    elif op[0] == "E":
        wx += op[1]
    elif op[0] == "W":
        wx -= op[1]
    elif op[0] == "F":
        x += op[1] * wx
        y += op[1] * wy
    elif op[0] == "L":
        for i in range(int(op[1] / 90)):
            tmp = wx
            wx = -wy
            wy = tmp
    elif op[0] == "R":
        for i in range(int(op[1] / 90)):
            tmp = wx
            wx = wy
            wy = -tmp
    else:
        print("ERROR  " + op)
        exit()
    print(str(x) + ", " + str(y) + "    " + str(wx) + ", " + str(wy))
print(abs(x) + abs(y))

#14min
