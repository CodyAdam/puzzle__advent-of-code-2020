IN = [int(x) for x in open("day10.txt", "r").read().splitlines()]

sort = sorted(IN)
current = 0
count = dict()

for x in sort:
    difference = x - current
    if (difference in count):
        count[difference] = count[difference] + 1
    else:
        count[difference] = 1
    current = x
count[3] = count[3] + 1

print(count)
print(count[1] * count[3])
#8 min
