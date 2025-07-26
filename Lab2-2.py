# Wczytanie komentarzy
print("Wprowadź 3 komentarze do analizy.")
komentarze = []
for i in range(3):
    # Prośba o wpisanie komentarza przez użytkownika
    komentarz = input(f"Podaj komentarz nr {i+1}: ")
    komentarze.append(komentarz)

# Utworzenie zbioru unikalnych słów
wszystkie_slowa = set()
for komentarz in komentarze:
    # Rozbicie komentarza na słowa i zamiana na małe litery
    slowa = komentarz.lower().split()
    # Dodanie słów do zbioru (set automatycznie dba o unikalność)
    wszystkie_slowa.update(slowa)

#Analiza i wyświetlanie wyników
print("\n--- Analiza Komentarzy ---")

# Wypisanie liczby unikalnych słów
print(f"✅ Liczba unikalnych słów we wszystkich komentarzach: {len(wszystkie_slowa)}")

# Wyszukanie i wypisanie słów dłuższych niż 5 liter
dlugie_slowa = {slowo for slowo in wszystkie_slowa if len(slowo) > 5}
print(f"✅ Słowa dłuższe niż 5 liter: {dlugie_slowa if dlugie_slowa else 'brak'}")

# Sprawdzenie obecności słowa "Python"
# Sprawdzamy, czy którekolwiek słowo w zbiorze to "python" lub pochodne
znaleziono_pythona = False
for slowo in wszystkie_slowa:
    if "python" in slowo:
        znaleziono_pythona = True
        break

if znaleziono_pythona:
    print("\n🐍 Uczestnicy lubią Pythona!")
