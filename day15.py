IN = open("day15.txt", "r").read().split(",")
for i in range(len(IN)):
    IN[i] = int(IN[i])


def count(x):
    first = len(IN) - 1
    second = None
    for i in range(1, len(IN)):
        i = len(IN) - 1 - i
        if (IN[i] == x):
            if second == None:
                second = i
            else:
                break
    if (second == None):
        return 0
    return first - second


while len(IN) < 2020:
    IN.append(count(IN[len(IN) - 1]))
print(IN)
print(IN[len(IN) - 1])
# 34min
