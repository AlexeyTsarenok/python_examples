produkty = ("mleko", "chleb", "masło", "ser", "jabłka", "pomidor", "cukier", "sól", "woda", "jogurt")

def stworz_koszyk(liczba_produktow=3):
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
    print(produkt)
