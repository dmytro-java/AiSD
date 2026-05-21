tablica = [3, 4, 1, 2, 5, 6, 7, 0]

szukanaLiczba = int(input("Podaj liczbe, a ja jej poszukam: "))

def szukamyLiczbe():
    for liczba in tablica:
        if liczba == szukanaLiczba:
            print("Liczba jest w tablicy")
            return
    print("Liczba nie jest w tablicy")
szukamyLiczbe()