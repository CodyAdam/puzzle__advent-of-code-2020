IN = [x.split("\n")[0] for x in open("day3.txt", "r").readlines()]
IN = [[char for char in IN[i]] for i in range(len(IN))]

h = len(IN)
w = len(IN[0])

cx = 0
cy = 0

right = 1
down = 2

tree = 0
notree = -1

while (cy < h):
    if (IN[cy][cx] == "#"):
        IN[cy][cx] = "X"
        tree += 1
    else:
        IN[cy][cx] = "O"
        notree += 1

    if cx + right >= w:
        cx -= w
    cx = (cx + right)
    cy = (cy + down)

print(tree)
#3 min