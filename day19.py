IN = [x for x in open("day19.txt", "r").read().splitlines()]

rules = []
toTest = None
for line in IN:
    rule = None
    state = 0
    if line is "":
        toTest = []
    elif toTest is not None:
        toTest.append(line)
    else:
        line = line.split(": ")[1].replace(" | ", "+").replace(" ", "*")
        line = line.replace("*", " * ").replace("+", " + ")
        rules.append(line)


def subStringify(str):
    parenth = None
    ans = []
    subStr = ""
    for char in str.split(" "):
        if char is "(":
            if parenth is not None:
                parenth += 1
                subStr += char
            else:
                parenth = 1
        elif char is ")":
            parenth -= 1
            if parenth is 0:
                ans.append(subStringify(subStr))
                subStr = ""
                parenth = None
            else:
                subStr += char
        elif parenth is not None:
            subStr += char
        else:
            ans.append(char)
    return ans


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


def draw():
    for rule in rules:
        print(rule)
    print()
    for line in toTest:
        print(line)


def verify(strTest, rule):
    if type(rule) is str:
        match = rule.replace("\"", "")
        our = strTest[0:len(match)]
        if our == match:
            return len(match)
        return 0
    elif len(rule) is 1:
        return verify(strTest, rule[0])

    for i in range(len(rule)):
        r = rule[i]
        if r is "*":
            first = verify(strTest, rule[i - 1])
            if first == 0:
                return 0
            second = verify(strTest[first:], rule[i + 1])
            if second == 0:
                return 0
            return first + second
        elif r is "+":
            first = verify(strTest, rule[i - 1])
            second = verify(strTest, rule[i - 1])
            return max(first, second)


for i in range(len(rules)):
    print(rules[i])
    rules[i] = subStringify(rules[i])
    rules[i] = applyPrecedence(rules[i])
rules[0] = replaceIndex(rules[0])
print(rules[0])

for test in toTest:
    print(verify(test, rules[0]))
