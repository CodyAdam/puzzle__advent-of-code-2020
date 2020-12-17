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


def verifLine(str):
    arr = [int(x) for x in str.split(",")]
    ans = []
    found = False
    for x in arr:
        found = False
        for key in ranges:
            if found:
                continue
            if x in ranges[key]:
                found = True
        if not found:
            ans.append(x)
    return ans


IN = init()
ranges = setRanges()

ans = []
for line in IN[2]:
    if line == "nearby tickets:":
        continue
    ans.append(verifLine(line))

sum = 0
for x in ans:
    for y in x:
        sum += y
print(sum)
#1h