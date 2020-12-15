IN = [x for x in open("day13.txt", "r").read().splitlines()]

timestamp = 1
increment = 1
offset = 0
id = IN[1].split(",")

while (offset < len(id)):

    if (id[offset] == "x"):
        offset += 1
        continue

    if ((timestamp + offset) % int(id[offset]) == 0):
        print("INCREMENT " + str(int(id[offset]) * increment) + " offset = " +
              str(offset))
        increment = int(id[offset]) * increment
        offset += 1

    print(timestamp)
    timestamp += increment

print("EXIT " + str(timestamp - increment))

#2h08min