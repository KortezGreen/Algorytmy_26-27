def quick_sort(dane):
    wynik = dane.copy()
    _quick_sort(wynik, 0, len(wynik) - 1)
    return wynik


def _quick_sort(tablica, low, high):
    if low > high:
        return 0
    # Podziel zakres i zapamiętaj indeks pivota.
    pivot_index = _partition(tablica, low, high)

    # Posortuj rekurencyjnie część przed pivotem.
    _quick_sort(tablica, low, pivot_index - 1)

    # Posortuj rekurencyjnie część za pivotem.
    _quick_sort(tablica, pivot_index + 1, high)
    pass


def _partition(tablica, low, high):  # _ sygnalizuje funkcję pomocniczą (konwencja Pythona)
    # Wybieramy ostatni element jako pivot (schemat Lomuto).
    pivot = tablica[high]

    # Indeks granicy dla elementów mniejszych lub równych pivotowi.
    i = low - 1

    for j in range(low, high):
        # Jeśli bieżący element jest mniejszy lub równy pivotowi, przesuwamy go na lewo.
        if tablica[j] <= pivot:
            i += 1
            tablica[i], tablica[j] = tablica[j], tablica[i]

    # Wstawiamy pivot na jego właściwe, posortowane miejsce.
    tablica[i + 1], tablica[high] = tablica[high], tablica[i + 1]

    # Zwracamy ostateczny indeks pivota.
    return i + 1

tab = [2, 7, 9, 4, 3, 8, 5]
print("P1:",tab)
print("P2:",quick_sort(tab))
