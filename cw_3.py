import random
import time
import statistics

def zmierz_czas(funkcja, dane, powtorzenia=5):
    czasy = []

    for _ in range(powtorzenia):
        kopia = dane.copy()

        start = time.perf_counter()
        funkcja(kopia)
        koniec = time.perf_counter()

        czasy.append(koniec - start)

    return statistics.median(czasy)

def selection_sort_bez_optymalizacji(lista):
    n = len(lista)
    for i in range(0, n-1, 1):
        min = i
        for j in range(i+1, n, 1):
            if(lista[j]<lista[min]):
                min = j
        lista[i], lista[min] = lista[min], lista[i]
    return lista

def selection_sort_z_optymalizacja(lista):
    n = len(lista)
    for i in range(0, n-1, 1):
        min = i
        for j in range(i+1, n, 1):
            if(lista[j]<lista[min]):
                min = j
        if (min != i):
            lista[i], lista[min] = lista[min], lista[i]
    return lista

def selection_sort_z_optymalizacja2(lista):
    n = len(lista)
    for i in range(0, n//2, 1):
        min = i
        max = i
        prawy_kraniec = n - 1 - i
        for j in range(i + 1, prawy_kraniec + 1, 1):
            if(lista[j] < lista[min]):
                min = j
            if(lista[j] > lista[max]):
                max = j
        if (min != i):
            lista[i], lista[min] = lista[min], lista[i]
        if max == i:
            max = min
        if (max != prawy_kraniec):
            lista[prawy_kraniec], lista[max] = lista[max], lista[prawy_kraniec]
    return lista


if __name__ == '__main__':
    print(selection_sort_bez_optymalizacji([5, 2, 8, 1, 4]))
    # Oczekiwany wynik: [1, 2, 4, 5, 8]

    print(selection_sort_bez_optymalizacji([7, 3, 5, 2, 1]))
    # Oczekiwany wynik: [1, 2, 3, 5, 7]

    print(selection_sort_bez_optymalizacji([1, 2, 3, 4, 5]))
    # Oczekiwany wynik: [1, 2, 3, 4, 5]

    print(selection_sort_bez_optymalizacji([5, 4, 3, 2, 1]))
    # Oczekiwany wynik: [1, 2, 3, 4, 5]

    print(selection_sort_bez_optymalizacji([]))
    # Oczekiwany wynik: []

    for n in [500, 1000, 2000]:
        dane = {
            "losowe": random.sample(range(n * 10), n),
            "rosnace": list(range(n)),
            "malejace": list(range(n, 0, -1))
        }

        print(f"\nRozmiar listy: {n}")

        for nazwa, lista in dane.items():
            t1 = zmierz_czas(selection_sort_bez_optymalizacji, lista)
            t2 = zmierz_czas(selection_sort_z_optymalizacja, lista)
            t3 = zmierz_czas(selection_sort_z_optymalizacja2, lista)

            print(
                f"{nazwa:10} | "
                f"bez opt.: {t1 * 1000:.3f} ms | "
                f"z opt.: {t2 * 1000:.3f} ms | "
                f"z opt. 2: {t3 * 1000:.3f} ms"
            )
