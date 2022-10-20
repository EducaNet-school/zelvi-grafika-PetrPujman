s = ["Franta", "Pepa", "Vašek", "Ignác"]


def od1():
    global s
    s.append(input("napiš další jméno"))
    otazka()


def od2():
    global s
    print(s)
    s.remove(input("napis jmeno"))
    otazka()


def od3():
    global s
    print(s)
    otazka()


def od4():
    global s
    print("v seznamu je", len(s), "jmen")
    otazka()


def od5():
    global s
    s.sort()
    print(s)
    otazka()


def od6():
    print("ok")


def otazka():
    global s
    print("1.Pridat jmeno")
    print("2.odebrat jmeno")
    print("3.vypsat seznam")
    print("4.kolik je jmen v seznamu")
    print("5.seznam jsem podle abecedy")
    print("6.konec programu")
    o = int(input("vyber"))
    if o == 1:
        od1()
    if o == 2:
        od2()
    if o == 3:
        od3()
    if o == 4:
        od4()
    if o == 5:
        od5()
    elif o == 6:
        od6()


otazka()
