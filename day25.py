def loopSize(subject, times):
    value = 1
    for _ in range(times):
        value *= subject
        value = value % 20201227
    return value


def getLoopFromPublic(x):
    for i in range(0, 100000):
        if loopSize(7, i) == x:
            return i
    return -1


def findSize(x):
    # x = 14505727
    size = 0
    while x > 1:
        size += 1
        while x % 7 != 0:
            x += 20201227
        x /= 7
        print(round(size * 1000 / 20201227) / 10)
    print(size)
    return size


# findSize(16616892)
print(loopSize(7, 4711642))