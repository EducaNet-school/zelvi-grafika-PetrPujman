s = [" ", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět", "deset", "jedenáct", "dvanáct",
     "třináct", "čtrnáct", "patnáčct", "šestnáct", "sedmnáct", "osmnáct", "devatenácat"]

desitky = [" ", " ", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]


def cisla():
    cislo = int(input("zadej číslo od jedné do 99"))

    if cislo < 20:
        print(s[cislo])
    elif cislo <= 99:
        if cislo >= 90:
            print(desitky[9])
            cislo -= 90
            print(s[cislo])
        if cislo >= 80:
            print(desitky[8])
            cislo -= 80
            print(s[cislo])
        if cislo >= 70:
            print(desitky[7])
            cislo -= 70
            print(s[cislo])
        if cislo >= 60:
            print(desitky[6])
            cislo -= 60
            print(s[cislo])
        if cislo >= 50:
            print(desitky[5])
            cislo -= 50
            print(s[cislo])
        if cislo >= 40:
            print(desitky[4])
            cislo -= 40
            print(s[cislo])
        if cislo >= 30:
            print(desitky[3])
            cislo -= 30
            print(s[cislo])
        if cislo >= 20:
            print(desitky[2])
            cislo -= 20
            print(s[cislo])
    else:
        print("zadané číslo není od jedné do 99")
        cisla()


cisla()
