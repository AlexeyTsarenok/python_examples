''' Zadanie 2: Formatowanie tekstu 

Napisz funkcję formatuj(tekst), która: 

usunie nadmiarowe spacje z początku i końca tekstu, 

zamieni wszystkie litery na małe, 

zamieni w tekście słowo “python” na “PYTHON”. ''' 

def formatuj(tekst):
    tekst = tekst.strip()  # Usuwa nadmiarowe spacje z początku i końca
    tekst = tekst.lower()  # Zamienia wszystkie litery na małe
    tekst = tekst.replace("python", "PYTHON")  # Zamienia "python" na "PYTHON"
    return tekst

# Przykładowe użycie
tekst = "  Python jest świetnym językiem programowania. "
sformatowany_tekst = formatuj(tekst)

print(sformatowany_tekst)  # Wyświetli: "python jest świetnym językiem programowania."
