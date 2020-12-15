IN = open("day15.txt", "r").read().split(",")

k = dict()

for i in range(len(IN) - 1):
    k[int(IN[i])] = i + 1

turn = len(IN)
current = int(IN[len(IN) - 1])

print(k)
while turn < 30000000:
    if current in k:
        tmp = k[current]
        k[current] = turn
        current = turn - tmp
    else:
        k[current] = turn
        current = 0
    turn += 1

print(current)