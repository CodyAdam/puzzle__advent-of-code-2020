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


sum = 0
for line in IN:
    arr = subStringify(line)
    print(line)
    sum += calc(arr)
    print(calc(arr))
print(sum)

# 52 min