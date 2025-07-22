import datetime

CENA_NORMALNEGO = 30
CENA_STUDENCKIEGO = 20
CENA_SENIORA = 15
ZNIZKA_SRODOWA = 5
DNI_TYGODNIA = [
    "poniedziałek", "wtorek", "środa", "czwartek", "piątek", "sobota", "niedziela"
]

def pobierz_wiek():
    while True:
        try:
            wiek = int(input("Proszę podać swój wiek: "))
            if wiek > 0:
                return wiek
            else:
                print("Wiek musi być liczbą dodatnią. Spróbuj ponownie.")
        except ValueError:
            print("To nie jest poprawny wiek. Proszę wpisać liczbę.")

def pobierz_status_studenta():
    while True:
        odp = input("Czy jesteś studentem? (tak/nie): ").lower()
        if odp in ["tak", "nie"]:
            return odp == "tak"
        print("Proszę odpowiedzieć 'tak' lub 'nie'.")

def pobierz_dzien_tygodnia():
    # Automatycznie pobiera dzień tygodnia z systemu
    dzien_index = datetime.datetime.today().weekday()  # 0=poniedziałek, 6=niedziela
    return DNI_TYGODNIA[dzien_index]

def oblicz_cene_biletu():
    print("Witaj w systemie biletowym Multikina!")
    wiek = pobierz_wiek()
    jest_studentem = pobierz_status_studenta()
    dzien_tygodnia = pobierz_dzien_tygodnia()
    print(f"Dziś jest: {dzien_tygodnia.capitalize()}")

    if wiek <= 4:
        cena_biletu = 0
        print("\nDzieci do lat 4 wchodzą za darmo!")
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
