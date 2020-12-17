IN = [[y for y in x] for x in open("day17.txt", "r").read().splitlines()]

size = len(IN)
grid = [[[["." for x in range(size)] for y in range(size)]
         for z in range(size)] for w in range(size)]

for y in range(size):
    for x in range(size):
        grid[int(size / 2)][int(size / 2)][y][x] = IN[y][x]


def draw(theGrid):
    for w in range(len(theGrid)):
        for z in range(len(theGrid)):
            print("z = " + str(z - int(size / 2)) + " w = " +
                  str(w - int(size / 2)))
            for line in theGrid[w][z]:
                s = ""
                for char in line:
                    s += char + " "
                print(s)
            print()
    print("##################################")


def expand():
    global size
    global grid
    size += 2
    newGrid = [[[["." for x in range(size)] for y in range(size)]
                for z in range(size)] for w in range(size)]

    for w in range(size):
        for z in range(size):
            for y in range(size):
                for x in range(size):
                    if (w - 1 in range(size - 2) and z - 1 in range(size - 2)
                            and y - 1 in range(size - 2)
                            and x - 1 in range(size - 2)):
                        newGrid[w][z][y][x] = grid[w - 1][z - 1][y - 1][x - 1]

    grid = newGrid


def tick():
    global size
    global grid
    newGrid = [[[[grid[w][z][y][x] for x in range(size)] for y in range(size)]
                for z in range(size)] for w in range(size)]

    for w in range(size):
        for z in range(size):
            for y in range(size):
                for x in range(size):
                    if (grid[w][z][y][x] == "#"):
                        if (countActive(x, y, z, w) in range(2, 3 + 1)):
                            continue
                        else:
                            newGrid[w][z][y][x] = "."
                    else:
                        if (countActive(x, y, z, w) is 3):
                            newGrid[w][z][y][x] = "#"
                        else:
                            continue
    grid = newGrid


def countActive(cx, cy, cz, cw):
    global grid
    count = 0

    for w in range(max(0, cw - 1), min(size, cw + 2)):
        for z in range(max(0, cz - 1), min(size, cz + 2)):
            for y in range(max(0, cy - 1), min(size, cy + 2)):
                for x in range(max(0, cx - 1), min(size, cx + 2)):
                    if (x == cx and cy == y and cz == z and cw == w):
                        continue
                    if (grid[w][z][y][x] == "#"):
                        count += 1
    return count


def isBordered():
    for w in range(size):
        for z in range(size):
            for y in range(size):
                for x in range(size):
                    if (z == 0 or z == size - 1 or y == 0 or y == size - 1
                            or x == 0 or x == size - 1 or w == 0
                            or w == size - 1) and grid[w][z][y][x] == "#":
                        return True
    return False


def count():
    count = 0
    for w in range(size):
        for z in range(size):
            for y in range(size):
                for x in range(size):
                    if grid[w][z][y][x] == "#":
                        count += 1
    return count


draw(grid)

for cycle in range(6):
    print("After " + str(cycle + 1) + " cycle")
    if (isBordered()):
        expand()
        expand()
    tick()
    draw(grid)
print("Actives number = " + str(count()))

#18 min
