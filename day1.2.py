IN = [int(x) for x in open("day1.txt", "r").readlines()]


def found(x):
    for num in IN:
        if num == x:
            return True
    return False


for num1 in IN:
    for num2 in IN:
        num3 = (2020 - num1 - num2)
        if (found(num3)):
            print(num1 * num2 * num3)
            exit()

#4 min
