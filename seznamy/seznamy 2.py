list = [0, 1]
pocet = int(input("zadej pocet cisel"))
y = 0
z = 1
for i in range(pocet):
    x = list[y] + list[z]
    y += 1
    z += 1
    list.append(x)

print(list)
# rada zacina od 1
