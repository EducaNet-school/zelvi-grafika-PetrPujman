cislo = int(input("zadej lyche číslo"))

if cislo % 2 == 0:
    cislo += 1

list = [cislo]

for i in range(9):
    cislo += 2
    list.append(cislo)
print(list)
