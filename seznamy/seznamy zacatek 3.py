cislo = int(input("zadej liche cislo"))
list = [cislo]
x = cislo

for i in range(7):
    x += 2
    list.append(x)

soucet = sum(list)
print(list)
print(soucet)
