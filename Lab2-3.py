# Firma przeprowadziła test wiedzy dla nowych pracowników. Wyniki zapisano w tupli:
# wyniki = (45, 67, 82, 90, 55, 74, 100, 61)
# Napisz program, który:
# Policz i wypisz średnią ocen.
# Wypisz wszystkie wyniki powyżej średniej.
# Wypisz ile osób zdało test (wynik >= 60).
# Jeśli ktoś zdobył 100 punktów, wypisz komunikat: „Gratulacje dla najlepszego uczestnika!”.

wyniki = (45, 67, 82, 90, 55, 74, 100, 61)
srednia = sum(wyniki) / len(wyniki)

wyniki_powyzej_sredniej = [wynik for wynik in wyniki if wynik > srednia]

zdalo_test = sum(1 for wynik in wyniki if wynik >= 60)

print(f"Średnia ocen: {srednia:.2f}")
print("Wyniki powyżej średniej:", wyniki_powyzej_sredniej)
print(f"Liczba osób, które zdały test: {zdalo_test}")
if 100 in wyniki:
    print("Gratulacje dla najlepszego uczestnika!")
