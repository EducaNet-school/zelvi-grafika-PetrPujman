s = [100, 500]

n = int(input("zadej cislo"))

if min(s) > n:
    print("všechna čísla v seznamu jsou větší než", n)
elif max(s) < n:
    print("všechna čísla v seznamu jsou menší než", n)
else:
    print(n, "není ani větší ani menší než všechna čísla v seznamu")
