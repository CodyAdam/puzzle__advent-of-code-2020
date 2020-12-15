IN = [x for x in open("day13.txt", "r").read().splitlines()]

startTimestamp = int(IN[0])
timestamp = startTimestamp
bus = IN[1].split(",")

while (True):
    for b in bus:
        if (b == "x"):
            continue
        if (timestamp % int(b) == 0):
            print(b + "  " + str(int(b) * (timestamp - startTimestamp)))
            exit()
    timestamp += 1
#8 min