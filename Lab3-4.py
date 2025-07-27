''' Zadanie 4: Odwracanie słów 
Napisz funkcję odwroc_slowa(zdanie), która: 
- rozbije zdanie na słowa (split), 
- odwróci każde słowo osobno (np. "Ala ma kota" → "alA am atok"), 
- połączy słowa w nowy string i zwróci wynik. ''' 

def odwroc_slowa(zdanie):
    slowa = zdanie.split()
    odwrocone_slowa = [slowo[::-1] for slowo in slowa]
    return ' '.join(odwrocone_slowa)

# Przykładowe użycie
zdanie = "Ala ma kota"
wynik = odwroc_slowa(zdanie)
print(wynik)  # "alA am atok"