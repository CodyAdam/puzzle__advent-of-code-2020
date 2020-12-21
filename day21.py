IN = [x for x in open("day21.txt", "r").read().splitlines()]

foods = []
assoc = {}
allIngredients = set()
cantContain = set()


def init():
    for line in IN:
        line = line.replace(" (contains ", ";").replace(", ",
                                                        " ").replace(")", "")
        foods.append([x.split(" ") for x in line.split(";")])


def associate():
    global allIngredients
    for ingredients, allergens in foods:
        allIngredients = allIngredients.union(set(ingredients))
        for allergen in allergens:
            if allergen in assoc:
                assoc[allergen] = assoc[allergen].intersection(
                    set(ingredients))
            else:
                assoc[allergen] = set([x for x in ingredients])


def removeUseless():
    for key in assoc:
        if len(assoc[key]) == 1:
            for k in assoc:
                if (k != key):
                    assoc[k] = assoc[k] - assoc[key]


def getAppear(s):
    sum = 0
    for elem in s:
        for ingredients, allergens in foods:
            if elem in ingredients:
                sum += 1
    return sum


init()
associate()
print(assoc)
removeUseless()
print(assoc)

cantContain = set(allIngredients)
for key in assoc:
    cantContain = cantContain - assoc[key]
print(cantContain)
print(len(cantContain))
print(getAppear(cantContain))
#30min