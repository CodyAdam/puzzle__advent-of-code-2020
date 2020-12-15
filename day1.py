IN = [int(x) for x in open("day1.txt", "r").readlines()]


def found(x):
    for num in IN:
        if num == x:
            return True
    return False


for num in IN:
    if (found(2020 - num)):
        print(num * (2020 - num))
        exit()

#12 min
