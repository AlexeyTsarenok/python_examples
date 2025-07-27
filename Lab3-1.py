''' Zadanie 1: Licznik liter 

Napisz funkcję licz_litery(tekst), która: 

przyjmie string, 

zwróci słownik z liczbą wystąpień każdej litery (ignorując wielkość liter i znaki interpunkcyjne), 

wypisze wynik w formie: 

a: 3 
b: 1 
''' 

from collections import defaultdict

def licz_litery(tekst):
    tekst = tekst.lower()
    licznik = defaultdict(int)
    for char in tekst:
        if char.isalpha():
            licznik[char] += 1
    return licznik

# Przykładowe użycie
tekst = "Ala ma kota, a kot ma Ale!"
wynik = licz_litery(tekst)
for litera in sorted(wynik):
    print(f"{litera}: {wynik[litera]}")

