import re
IN = [x for x in open("day4.txt", "r").read().splitlines()]
n = 0


def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct


for line in IN:
    if (line == ""):
        n += 1

ans = [""] * (n + 1)
n = 0
for line in IN:
    if (line == ""):
        n += 1
        continue
    if (n < len(ans)):
        ans[n] += line + " "

for i in range(len(ans)):
    ans[i] = re.split(" |:", ans[i])
    ans[i].pop()
    ans[i] = Convert(ans[i])

EYECOLORS = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def byr(cred):
    return "byr" in cred and (int(cred["byr"]) in range(1920, 2003)) and len(
        cred["byr"]) == 4


def iyr(cred):
    return (("iyr" in cred) and int(cred["iyr"]) in range(2010, 2021)) and len(
        cred["iyr"]) == 4


def eyr(cred):
    return (("eyr" in cred) and int(cred["eyr"]) in range(2020, 2031)) and len(
        cred["eyr"]) == 4


def hgt(cred):
    if ("hgt" in cred):
        print("------")
        print(cred["hgt"])
        if (re.search("[a-z]{2}$", cred["hgt"])
                and re.search("^[0-9]+", cred["hgt"])):
            unit = re.findall("[a-z]{2}$", cred["hgt"])
            value = re.findall("^[0-9]+", cred["hgt"])

            print(unit)
            print(value)

            if unit[0] == "cm" and int(value[0]) in range(150, 194):
                return True
            if unit[0] == "in" and int(value[0]) in range(59, 77):
                return True
    return False


def hcl(cred):
    if (("hcl" in cred) and re.search("#\w{6}", cred["hcl"])):
        return True
    else:
        False


def ecl(cred):
    return (("ecl" in cred) and cred["ecl"] in EYECOLORS)


def pid(cred):
    return (("pid" in cred) and re.search("^[0-9]{9}", cred["pid"])
            and len(cred["pid"]) == 9)


sum = 0

for cred in ans:
    if (byr(cred) and iyr(cred) and eyr(cred) and hcl(cred) and ecl(cred)
            and pid(cred) and hgt(cred)):
        sum += 1
print(sum)