IN = [x for x in open("day18.txt", "r").read().splitlines()]


def calc(arr):
    state = 0
    ans = 0
    if type(arr) is str:
        return arr

    for i in range(len(arr)):
        char = calc(arr[i])
        if state is 0:
            ans += int(char)
            state = 1
        elif state is 1 and char is "+":
            i += 1
            ans += int(calc(arr[i]))
            i += 1

        elif state is 1 and char is "*":
            i += 1
            ans *= int(calc(arr[i]))
            i += 1
    return ans


def subStringify(str):
    parenth = None
    ans = []
    subStr = ""
    for char in str:
        if char is " ":
            continue
        elif char is "(":
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
        if curr is "+":
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


sum = 0
for line in IN:
    arr = subStringify(line)
    arr = applyPrecedence(arr)
    print(arr)
    print(calc(arr))
    sum += calc(arr)
print(sum)
# 29 min