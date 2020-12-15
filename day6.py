IN = [x for x in open("day6.txt", "r").read().splitlines()]
n = 0
for line in IN:
    if (line == ""):
        n += 1

groups = [""] * (n + 1)
n = 0
for line in IN:
    if (line == ""):
        n += 1
        continue
    if (n < len(groups)):
        groups[n] += line + " "


def getUnique(str):
    s = set()
    for char in str:
        if char == " ":
            continue
        if char not in s:
            s.add(char)
    return len(s)


sum = 0
for g in groups:
    sum += getUnique(g)
print(sum)

#12 min