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


SAVE = IN.copy()
runned = set()
accumulator = 0

for index, line in enumerate(SAVE):
    if (line[0] == "jmp"):
        replace = ["nop", line[1]]
    elif (line[0] == "nop"):
        replace = ["jmp", line[1]]
    else:
        continue
    IN = SAVE.copy()
    runned = set()
    accumulator = 0
    IN[index] = replace
    ans = operator()
    if (ans[0] == "STOP"):
        print(ans)

#29min