IN = [int(x) for x in open("day9.txt", "r").read().splitlines()]

target = 26134589

for i in range(len(IN)):
    sum = 0
    list = []
    if (IN[i] >= target):
        continue
    sum += IN[i]
    list.append(IN[i])
    if (i + 1 >= len(IN)):
        print("OUT OF LINE")
    for j in range(i + 1, len(IN)):
        if (sum == target):
            print(list)
            print(int(min(list) + max(list)))

        elif (sum > target):
            break
        sum += IN[j]
        list.append(IN[j])
#12 min