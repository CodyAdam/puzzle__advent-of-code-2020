IN = open("day23.txt", "r").read()
print(IN)


class CircularList:
    class Element:
        def __init__(self, x):
            self.next = None
            self.prev = None
            self.value = x

    def __init__(self):
        self.first = None
        self.current = None
        self.max = 0
        self.rep = {}

    def add(self, x):
        if self.first == None:
            self.first = self.Element(x)
            self.first.next = self.first
            self.first.prev = self.first
            self.current = self.first
            self.max = self.first.value
            self.rep[x] = self.first
        else:
            if x > self.max:
                self.max = x
            newElem = self.Element(x)
            newElem.next = self.first
            newElem.prev = self.first.prev
            self.first.prev.next = newElem
            self.first.prev = newElem
            self.rep[x] = newElem

    def found(self, x):
        return self.rep[x]

    def foundDestination(self, current):
        dontPick = [
            current.next.value, current.next.next.value,
            current.next.next.next.value
        ]
        value = current.value - 1 if current.value > 1 else self.max
        while value in dontPick:
            value = value - 1 if value > 1 else self.max

        return self.found(value)

    def moveThree(self, current, destination):
        group = current.next

        current.next = current.next.next.next.next
        current.next.prev = current

        destination.next.prev = group.next.next
        destination.next.prev.next = destination.next

        destination.next = group
        group.prev = destination

    def getResult(self):
        # s = ""
        current = self.found(1).next
        # while current.next.value is not 1:
        #     s += str(current.value)
        #     current = current.next
        # s += str(current.value)
        # return s
        print(current.value)
        print(current.next.value)
        return current.value * current.next.value

    def __str__(self):
        s = ""
        current = self.first
        i = 0
        while current.next is not self.first and i < 20:
            s += str(current.value) + ", "
            i += 1
            current = current.next
        s += str(current.value)
        if i >= 20:
            s += " .... "
        return s


circ = CircularList()

for x in IN:
    circ.add(int(x))
for x in range(circ.max + 1, 1000001):
    circ.add(int(x))
print(circ)

for _ in range(10000000):
    destination = circ.foundDestination(circ.current)
    circ.moveThree(circ.current, destination)
    circ.current = circ.current.next
print(circ.getResult())
#45 min