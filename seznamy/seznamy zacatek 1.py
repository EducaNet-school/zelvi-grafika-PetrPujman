list = []
list2 = []
pocet = int(input("kolik prvocisel?"))
for cislo in range(1, 1000):
    if cislo > 1: #zacni range od 2 a muzes vyhodit podminku
        for i in range(2, cislo):
            if (cislo % i) == 0:
                break
        else:
            list.append(cislo)

for i in range(pocet):
    list2.append(list[i])

print(list2)
# je to dobre, ale zbutecne presypas seznamy, mrkni na poznamku na radku 5

