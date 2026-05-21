import bubble_sort

tablica = [1, 3, 2, 6, 7, 0]

szukana = int(input("podaj liczbe, a ja poszukam \n"))

tablica, ileRazy = bubble_sort.bubble_sort(tablica)
print(f"Posortowana tablica:  {tablica}")
left = 0
right = len(tablica) - 1
czyJest = False

while left <= right:
    mid = (left + right) //  2
    if tablica[mid] == szukana:
        czyJest = True
        break
    
    if tablica [mid] < szukana:
        left = mid + 1
    else:
        right = mid - 1


odp = "tak" if czyJest else "nie"
print(f"czy znalezlismy liczbe {szukana}? {odp}")
print(f"ile iteracji: {ileRazy}")
