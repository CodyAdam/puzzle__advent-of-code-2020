IN = [x for x in open("day20.txt", "r").read().splitlines()]

tiles = {}
size = len(IN[2])


def init():
    global tiles

    curr = {}
    id = ""
    grid = []
    for line in IN:
        if "Tile" in line:
            id = int(line.replace("Tile ", "").replace(":", ""))
        elif line == "":
            curr["grid"] = [[char for char in y] for y in grid]
            tiles[id] = curr
            grid = []
            curr = {}
        else:
            grid.append(line)
    curr["grid"] = [[char for char in y] for y in grid]
    tiles[id] = curr


def draw():
    s = ""
    for id in tiles:
        s += "id : " + str(id) + "\n"
        tile = tiles[id]
        for y in tile["grid"]:
            for x in y:
                s += x
            s += "\n"
    print(s)


def getBorder():
    SIDES = [("top", range(size), [0]), ("right", [size - 1], range(size)),
             ("bot", range(size), [size - 1]), ("left", [0], range(size))]
    for tile in tiles:
        for side, rx, ry in SIDES:
            value = 0
            reversedValue = 0
            i = 0
            for y in ry:
                for x in rx:
                    if tiles[tile]["grid"][y][x] is "#":
                        value += pow(2, i)
                    i += 1
            i = 0
            for y in reversed(ry):
                for x in reversed(rx):
                    if tiles[tile]["grid"][y][x] is "#":
                        reversedValue += pow(2, i)
                    i += 1
            tiles[tile][side] = (value, reversedValue)


init()
draw()
getBorder()
print(tiles)
#45min