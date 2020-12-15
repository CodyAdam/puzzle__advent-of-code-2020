import re
IN = [x for x in open("day14.txt", "r").read().splitlines()]


def decimalToBinary(n):
    return bin(n).replace("0b", "")


def dec(str):
    return int(str, 2)


def applyMask(bina):
    for i in range(len(mask)):
        if (mask[i] == "0"):
            continue
        bina = bina[:i] + mask[i] + (bina[i + 1:] if i + 1 < len(mask) else "")
    return bina


def xCount(bina):
    sum = 0
    for char in bina:
        if char == "X":
            sum += 1
    return sum


def putAtAddress(addressBin, toPut):
    n = xCount(addressBin)
    for i in range(pow(2, n)):
        x = decimalToBinary(i)
        xReplacement = ["0"] * n
        for j in range(len(x)):
            xReplacement[j - len(x)] = x[j]
        print(xReplacement)

        xCounter = 0
        tempAdd = list(addressBin)
        for j in range(len(tempAdd)):
            if tempAdd[j] == "X":
                tempAdd[j] = xReplacement[xCounter]
                xCounter += 1
        newAddress = dec("".join(tempAdd))
        mem[newAddress] = int(toPut)


mem = dict()

for i in range(len(IN)):
    if IN[i][1] == 'a':
        mask = IN[i].split(" = ")[1]
        continue
    address, value = re.findall("\d+", IN[i])

    addBin = str(decimalToBinary(int(address)))
    binaire = applyMask("000000000000000000000000000000000000" [0:36 -
                                                                len(addBin)] +
                        addBin)
    putAtAddress(binaire, value)

print(mem)
sum = 0
for add in mem:
    sum += mem[add]
print(sum)
