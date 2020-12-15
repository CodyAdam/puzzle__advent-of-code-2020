IN = [x for x in open("day12.txt", "r").read().splitlines()]

OP = []
for i in range(len(IN)):
    OP.append([])
    OP[i].append(IN[i][0])
    OP[i].append(int(IN[i][1:]))

x = 0
y = 0
facing = 0
DIR = ["E", "S", "W", "N"]

for op in OP:
    if op[0] == "N":
        y += op[1]
    elif op[0] == "S":
        y -= op[1]
    elif op[0] == "E":
        x += op[1]
    elif op[0] == "W":
        x -= op[1]
    elif op[0] == "F":
        if (facing == 0):
            x += op[1]
        elif (facing == 1):
            y -= op[1]
        elif (facing == 2):
            x -= op[1]
        elif (facing == 3):
            y += op[1]
    elif op[0] == "L":
        facing = (facing - int(op[1] / 90)) % 4
    elif op[0] == "R":
        facing = (facing + int(op[1] / 90)) % 4

print(x)
print(y)
print(abs(x) + abs(y))

#13min
