#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def pobierz_wiek():
    while True:
        try:
            wiek = int(input("Proszę podać swój wiek: "))
            if wiek > 0:
                return wiek
            print("Wiek musi być liczbą dodatnią. Spróbuj ponownie.")
        except ValueError:
            print("To nie jest poprawny wiek. Proszę wpisać liczbę.")

def pobierz_tak_nie(pytanie):
    while True:
        odp = input(pytanie + " (tak/nie): ").strip().lower()
        if odp in ("tak", "nie"):
            return odp == "tak"
        print("Proszę odpowiedzieć 'tak' lub 'nie'.")

def pobierz_dzien_tygodnia():
    return input("Jaki jest dzisiaj dzień tygodnia? (np. poniedziałek): ").strip().lower()

def oblicz_cene_biletu():
    CENA_NORMALNEGO = 30
    CENA_STUDENCKIEGO = 20
    CENA_SENIORA = 15
    ZNIZKA_SRODOWA = 5

    print("Witaj w systemie biletowym Multikina!")

    wiek = pobierz_wiek()
    jest_studentem = pobierz_tak_nie("Czy jesteś studentem")
    dzien_tygodnia = pobierz_dzien_tygodnia()

    if wiek <= 4:
        print("\nDzieci do lat 4 wchodzą za darmo!")
        cena_biletu = 0
    elif jest_studentem and wiek <= 26:
        cena_biletu = CENA_STUDENCKIEGO
    elif wiek >= 65:
        cena_biletu = CENA_SENIORA
    else:
        cena_biletu = CENA_NORMALNEGO

    if dzien_tygodnia == "środa" and cena_biletu > 0:
        cena_biletu -= ZNIZKA_SRODOWA
        print("Dziś środa! Otrzymujesz 5 zł zniżki.")

    print("\n------------------------------------")
    print(f"Ostateczna kwota do zapłaty: {cena_biletu} zł")
    print("------------------------------------")

if __name__ == "__main__":
    oblicz_cene_biletu()