IN = [x for x in open("day21.txt", "r").read().splitlines()]

foods = []
assoc = {}


def init():
    for line in IN:
        line = line.replace(" (contains ", ";").replace(", ",
                                                        " ").replace(")", "")
        foods.append([x.split(" ") for x in line.split(";")])


def associate():
    global allIngredients
    for ingredients, allergens in foods:
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


def assocToSorted():
    ans = ""
    sort = sorted(assoc)
    for word in sort:
        ans += list(assoc[word])[0] + ","
    return ans


init()
associate()
removeUseless()
removeUseless()
removeUseless()

for key in assoc:
    print(key + "  : " + str(assoc[key]))

print(assocToSorted())
#18min