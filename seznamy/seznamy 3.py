list = [1, 2, 3, 4]

pocet = int(input("o kolik mist se ma seznam posunout?"))

list = list[pocet:] + list[:pocet]

print(list)
