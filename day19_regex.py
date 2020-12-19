import re
IN = [x for x in open("day19.txt", "r").read().splitlines()]
rules = {}
toTest = None
for line in IN:
    rule = None
    state = 0
    if line is "":
        toTest = []
    elif toTest is not None:
        toTest.append(line)
    else:
        index = int(line.split(": ")[0])
        line = line.split(": ")[1].replace(" | ", "+").replace(" ", "*")
        line = line.replace("*", " * ").replace("+", " + ")
        rules[index] = line


def applyPrecedence(arr):
    new = []
    if type(arr) is str:
        return arr
    i = 0

    while i in range(len(arr)):
        if i >= len(arr):
            break
        curr = applyPrecedence(arr[i])
        if curr is "*":
            prev = applyPrecedence(arr[i - 1])
            nex = applyPrecedence(arr[i + 1])

            new.append(prev)
            new.append(curr)
            new.append(nex)
            arr[i - 1] = new
            new = []
            arr.pop(i)
            arr.pop(i)
            i -= 1
        i += 1
    return arr


def replaceIndex(arr):
    if type(arr) is str:
        return arr
    newArr = []
    for i in range(len(arr)):
        sub = arr[i]
        if type(sub) is str and sub is not "*" and sub is not "+" and (
                "\"" not in sub):
            newArr.append(replaceIndex(rules[int(sub)]))
        else:
            newArr.append(replaceIndex(sub))
    return newArr


def stringify(arr):
    if type(arr) is str:
        return arr.replace("\"", "").replace("*", "").replace("+", "|")
    s = "("
    for sub in arr:
        s += stringify(sub)
    return s + ")"


for i in rules:
    print(rules[i])
    rules[i] = applyPrecedence(rules[i].split(" "))
rules[0] = replaceIndex(rules[0])

print(rules[0])
print(stringify(rules[0]))

reg = stringify(rules[0])

sum = 0
for t in toTest:
    # print(re.fullmatch(reg, t))
    if re.fullmatch(reg, t):
        sum += 1
print(sum)
#40 min