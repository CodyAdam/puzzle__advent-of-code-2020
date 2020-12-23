IN = open("day23.txt", "r").read()
print(IN)
cups = [int(x) for x in IN]

currentIndex = 0
current = None
pickUp = []
destination = None

for move in range(100):
    if move + 1 == 9:
        print()

    current = cups[currentIndex]

    # pick up
    for i in range(1, 4):
        if currentIndex + i >= len(cups):
            pickUp.append(cups[i - (len(cups) - currentIndex)])
        else:
            pickUp.append(cups[currentIndex + i])

    print("Move : " + str(move + 1))
    print(cups)

    # remove picked up
    for _ in range(3):
        if currentIndex + 1 >= len(cups):
            cups.pop(1 - (len(cups) - cups.index(current)))
        else:
            cups.pop(cups.index(current) + 1)

    # find place
    found = False
    c = current - 1 if current is not 1 else max(cups)
    while found is False:
        for i in range(len(cups)):
            if c == cups[i]:
                destination = i + 1
                found = True
            elif c in pickUp:
                c = c - 1 if c is not 1 else max(cups)

    print(pickUp)
    print(cups[destination - 1])

    # place
    for x in reversed(pickUp):
        cups.insert(destination, x)

    pickUp = []
    currentIndex = 0 if cups.index(current) is (len(cups) -
                                                1) else cups.index(current) + 1

print(cups)
