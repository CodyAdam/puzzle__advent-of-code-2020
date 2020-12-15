IN = [int(x) for x in open("day10.txt", "r").read().splitlines()]

IN.append(0)
sort = sorted(IN)


def possibilities(currentIndex):
    ans = []
    for i in range(currentIndex + 1, len(sort)):
        if sort[i] - sort[currentIndex] in range(0, 4):
            ans.append(i)
        else:
            break
    return ans


print(sort)
alreadyCount = dict()


def get(currentIndex):
    possib = possibilities(currentIndex)
    sum = 0
    if len(possib) == 0:
        return 1
    for i in possib:
        if (i in alreadyCount):
            sum += alreadyCount[i]
        else:
            alreadyCount[i] = get(i)
            sum += alreadyCount[i]
    return sum


print(get(0))
#1h20min
