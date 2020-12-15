import re
IN = [x for x in open("day14.txt", "r").read().splitlines()]


def decimalToBinary(n):
    return bin(n).replace("0b", "")


def dec(str):
    return int(str, 2)


def applyMask(value):
    for i in range(len(mask)):
        if(mask[i] == "X"):
            continue
        value = value[:i] + mask[i] + (value[i+1:] if i+1 < len(mask) else "")
    return value


mem = dict()

for i in range(len(IN)):
    if IN[i][1] == 'a':
        mask = IN[i].split(" = ")[1]
        continue
    address, value = re.findall("\d+", IN[i])
    value = str(decimalToBinary(int(value)))
    mem[address] = "000000000000000000000000000000000000"[
        0:36-len(value)] + value
    mem[address] = applyMask(mem[address])


sum = 0
for add in mem:
    sum += dec(mem[add])
print(sum)
# 1h15 min
