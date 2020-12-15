import re
IN = [x for x in open("day2.txt", "r").readlines()]

count = 0

for i in range(len(IN)):
    (min, max, find, word) = re.findall("\w+", IN[i])

    if (word[int(min) - 1] == find or word[int(max) - 1] == find):
        if (word[int(min) - 1] != find or word[int(max) - 1] != find):

            count += 1

print(count)

#5 min
