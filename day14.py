from aocd import get_data

s = get_data(day=14,year=2018)
#first part
recipes = "37"
fst = 0
snd = 1

min_recipes = int(s)

while len(recipes)<min_recipes+10:
    summa = int(recipes[fst]) + int(recipes[snd])
    recipes += str(summa)
    fst = (fst+int(recipes[fst])+1)%len(recipes)
    snd = (snd+int(recipes[snd])+1)%len(recipes)

print("".join(recipes[min_recipes:min_recipes+10]))

#second part
recipes = "37"
fst = 0
snd = 1

while True:
    summa = int(recipes[fst]) + int(recipes[snd])
    recipes += str(summa)
    if recipes[-len(s):] == s or recipes[-len(s)-1:-1] == s:
        print(recipes.find(s))
        break
    fst = (fst+int(recipes[fst])+1)%len(recipes)
    snd = (snd+int(recipes[snd])+1)%len(recipes)