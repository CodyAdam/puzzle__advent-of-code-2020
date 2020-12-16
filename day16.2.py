IN = [line for line in open("day16.txt", "r").read().splitlines()]


def init():
    IN.append("")
    IN2 = []
    sub = []
    for line in IN:
        if (line == ""):
            IN2.append(sub)
            sub = []
            continue
        sub.append(line)
    return IN2


def setRanges():
    ranges = dict()
    for str in IN[0]:
        field = str.split(": ")[0]
        rangeStr = str.split(": ")[1]

        fieldRange = []
        for subRange in rangeStr.split(" or "):
            fieldRange.append(
                set(
                    range(int(subRange.split("-")[0]),
                          int(subRange.split("-")[1]) + 1)))
        joinedFieldRange = set()
        for x in fieldRange:
            joinedFieldRange = joinedFieldRange.union(x)
        ranges[field] = joinedFieldRange
    return ranges


def removeInvalid(line):
    arr = [int(x) for x in line.split(",")]
    ans = []
    found = False
    for i in range(len(arr)):
        found = False
        for key in ranges:
            if arr[i] in ranges[key]:
                found = True
        if not found:
            IN2.remove(line)


def invalid():

    for line in IN[2]:
        if line == "nearby tickets:":
            continue
        removeInvalid(line)
    IN[2] = IN2


def foundField(x):
    ans = []
    for key in ranges:
        if x in ranges[key]:
            ans.append(key)
    return set(ans)


def associate():
    for line in IN[2]:
        if line == "nearby tickets:":
            continue

        arr = [int(x) for x in line.split(",")]
        ans = []
        found = False
        for i in range(len(arr)):
            founded = foundField(arr[i])
            if i in assoc:
                assoc[i] = founded.intersection(assoc[i])
                removeUseless()
            else:
                assoc[i] = founded
                removeUseless()


def removeUseless():
    for index in assoc:
        value = assoc[index]
        if len(value) == 1:
            for i in assoc:
                if i == index:
                    continue
                assoc[i] = assoc[i] - value


assoc = dict()
IN = init()
IN2 = [x for x in IN[2]]
ranges = setRanges()
invalid()  #remove invalids

print(IN)
associate()
print(assoc)

myTi = [int(x) for x in IN[1][1].split(",")]
print(myTi)
print(myTi[12] * myTi[8] * myTi[10] * myTi[13] * myTi[14] * myTi[16])
