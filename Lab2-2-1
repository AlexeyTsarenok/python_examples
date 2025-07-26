import string

print("Wprowadź 3 komentarze do analizy.")
komentarze = []
for i in range(3):
    komentarz = input(f"Podaj komentarz nr {i+1}: ")
    komentarze.append(komentarz)

# Utworzenie zbioru unikalnych słów
wszystkie_slowa = set()
for komentarz in komentarze:
    # Usuwanie interpunkcji i rozbicie na słowa
    slowa = komentarz.lower().translate(str.maketrans('', '', string.punctuation)).split()
    wszystkie_slowa.update(slowa)

print("\n--- Analiza Komentarzy ---")
print(f"✅ Liczba unikalnych słów we wszystkich komentarzach: {len(wszystkie_slowa)}")

dlugie_slowa = {slowo for slowo in wszystkie_slowa if len(slowo) > 5}
print(f"✅ Słowa dłuższe niż 5 liter: {dlugie_slowa if dlugie_slowa else 'brak'}")

# Sprawdzenie obecności dokładnie słowa "python"
if "python" in wszystkie_slowa:
    print("\n🐍 Uczestnicy lubią Pythona!")
