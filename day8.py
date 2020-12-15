IN = [x.split(" ") for x in open("day8.txt", "r").read().splitlines()]
for i in range(len(IN)):
    IN[i][1] = int(IN[i][1])


def operator(line=0):
    global accumulator
    if (line >= len(IN)):
        return ("STOP", accumulator)
    op, value = IN[line]
    if (line in runned):
        return ("LOOP", accumulator)
    runned.add(line)

    if (op == "nop"):
        return operator(line + 1)
    elif (op == "acc"):
        accumulator += value
        return operator(line + 1)
    elif (op == "jmp"):
        return operator(line + value)


runned = set()
accumulator = 0

print(operator())
#24min