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


def needed(color):
    sum = 0
    line = find(color)
    for bag in line[1]:
        if (bag[1] == "other"):
            return 0
        sum += needed(bag[1]) * int(bag[0]) + int(bag[0])
    return sum


print(needed("shiny gold"))
#18 min
