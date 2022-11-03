veta = str(input("Zadej větu: "))
sez = {}

def razeni(a,c):
    for a in a:
        if a in c:
            c[a] += 1
        else:
            c[a] = 1
    print(c)

razeni(veta, sez)
