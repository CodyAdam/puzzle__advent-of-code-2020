import re
IN = [x for x in open("day2.txt", "r").readlines()]

count = 0

for i in range(len(IN)):
    (min, max, find, word) = re.findall("\w+", IN[i])
    if (word.count(find) in range(int(min), int(max) + 1)):
        count += 1

print(count)

#31 min
