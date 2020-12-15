IN = [x for x in open("day4.txt", "r").read().splitlines()]
n = 0
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

sum = 0
for line in ans:
    if (line.find("byr") != -1 and line.find("iyr") != -1
            and line.find("eyr") != -1 and line.find("hgt") != -1
            and line.find("hcl") != -1 and line.find("ecl") != -1
            and line.find("pid") != -1):
        sum += 1

print(sum)

#45 min