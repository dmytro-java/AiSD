import bubble_sort

tablicaDoTestow = [3, 4, 1, 2, 5, 6, 0, 7]

szukanaLiczba = int(input("Podaj liczbe, a ja jej poszukam: "))

tablicaDoTestow, count = bubble_sort.bubble_sort(tablicaDoTestow)

def wyszukiwanie_binarne(tablica, szukanaLiczba):
    lewy = 0
    prawy = len(tablica) - 1

    while lewy <= prawy:
        srodek = (lewy + prawy) // 2

        if tablica[srodek] == szukanaLiczba:
            return srodek

        if szukanaLiczba > tablica[srodek]:
            lewy = srodek + 1
        else:
            prawy = srodek - 1

    return -1

index = wyszukiwanie_binarne(tablicaDoTestow, szukanaLiczba)

print("Posortowana tablica: ", tablicaDoTestow)
print("Liczba sprawdzen sortowania: ", count)

if index != -1:
    print("Znaleziono liczbe na indeksie: ", index)
else:
    print("Nie znaleziono liczby")