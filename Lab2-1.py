produkty = ("mleko", "chleb", "masło", "ser", "jabłka", "pomidor", "cukier", "sól", "woda", "jogurt")
liczba_produktow = 3

print("Dostępne produkty w sklepie:")
for produkt in sorted(produkty):
    print("-", produkt)

def stworz_koszyk():
    koszyk = []
    i = 0
    while i < liczba_produktow:
        wybor = input(f"Podaj produkt nr {i+1}: ").strip().lower()
        if wybor in produkty:
            koszyk.append(wybor)
            i += 1
        else:
            print(f"Produkt '{wybor}' jest niedostępny.")
    return koszyk

koszyk = stworz_koszyk()

print("\nProdukty w koszyku (alfabetycznie):")
for produkt in sorted(koszyk):
    print("-", produkt)
