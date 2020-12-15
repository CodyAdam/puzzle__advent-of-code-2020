IN = [x.split(" ") for x in open("day8.txt", "r").read().splitlines()]
for i in range(len(IN)):
    IN[i][1] = int(IN[i][1])


class BootCode:
    def __init__(self, codeInput):
        self.origin = codeInput.copy()
        self.code = codeInput.copy()
        self.runned = set()
        self.accumulator = 0

    def reset(self):
        self.code = self.origin.copy()
        self.runned = set()
        self.accumulator = 0

    def replaceOP(self, index, op):
        self.code[index] = [op, self.code[index][1]]

    def run(self, line=0):
        if (line >= len(self.code)):
            return ("STOP", self.accumulator)
        op, value = self.code[line]
        if (line in self.runned):
            return ("LOOP", self.accumulator)
        self.runned.add(line)

        if (op == "nop"):
            return self.run(line + 1)
        elif (op == "acc"):
            self.accumulator += value
            return self.run(line + 1)
        elif (op == "jmp"):
            return self.run(line + value)


boot = BootCode(IN)
for index, line in enumerate(boot.code):
    if (line[0] == "jmp"):
        replace = "nop"
    elif (line[0] == "nop"):
        replace = "jmp"
    else:
        continue
    boot.reset()
    boot.replaceOP(index, replace)
    ans = boot.run()
    if (ans[0] == "STOP"):
        print(ans)
