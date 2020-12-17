IN = [[y for y in x] for x in open("day17.txt", "r").read().splitlines()]

size = len(IN)
grid = []
for i in range(int(size / 2)):
    grid.append([["." for y in range(size)] for x in range(size)])
grid.append(IN)
for i in range(int(size / 2)):
    grid.append([["." for y in range(size)] for x in range(size)])


def draw(theGrid):

    for z in range(len(theGrid)):
        print("z = " + str(z - int(size / 2)))
        for line in theGrid[z]:
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
    newGrid = []
    for z in range(size):
        newGrid.append([[
            grid[z - 1][y - 1][x - 1] if
            (z - 1 in range(size - 2) and y - 1 in range(size - 2)
             and x - 1 in range(size - 2)) else "." for x in range(size)
        ] for y in range(size)])
    grid = newGrid


def tick():
    global size
    global grid
    newGrid = [[[grid[z][y][x] for x in range(size)] for y in range(size)]
               for z in range(size)]

    for z in range(size):
        for y in range(size):
            for x in range(size):
                if (grid[z][y][x] == "#"):
                    if (countActive(x, y, z) in range(2, 3 + 1)):
                        continue
                    else:
                        newGrid[z][y][x] = "."
                else:
                    if (countActive(x, y, z) is 3):
                        newGrid[z][y][x] = "#"
                    else:
                        continue
    grid = newGrid


def countActive(cx, cy, cz):
    global grid
    count = 0
    for z in range(max(0, cz - 1), min(size, cz + 2)):
        for y in range(max(0, cy - 1), min(size, cy + 2)):
            for x in range(max(0, cx - 1), min(size, cx + 2)):
                if (x == cx and cy == y and cz == z):
                    continue
                if (grid[z][y][x] == "#"):
                    count += 1
    return count


def isBordered():
    for z in range(size):
        for y in range(size):
            for x in range(size):
                if (z == 0 or z == size - 1 or y == 0 or y == size - 1
                        or x == 0 or x == size - 1) and grid[z][y][x] == "#":
                    return True
    return False


def count():
    count = 0
    for z in range(size):
        for y in range(size):
            for x in range(size):
                if grid[z][y][x] == "#":
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

#55 min
