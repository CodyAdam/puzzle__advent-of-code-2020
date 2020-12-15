IN = [x for x in open("day7.txt", "r").read().splitlines()]

for i in range(len(IN)):
    IN[i] = IN[i].split(" bags contain ")
    IN[i][1] = IN[i][1].split(", ")
    for j in range(len(IN[i][1])):
        IN[i][1][j] = IN[i][1][j].split("bag")[0][:-1].split(" ", 1)


def find(str):
    for line in IN:
        if (line[0] == str):
            return line
    print("NOT FOUND : " + str)


def getShiny(color):
    sum = 0
    line = find(color)
    if (line[0] == "shiny gold"):
        return 1
    for bag in line[1]:
        if (bag[1] == "other"):
            return 0
        sum += getShiny(bag[1]) * int(bag[0])
    return 1 if sum > 0 else 0


sum = 0
for line in IN:
    if (line[0] == "shiny gold"):
        continue
    sum += getShiny(line[0])
print(sum)
#25 min
