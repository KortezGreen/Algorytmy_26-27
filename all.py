class BubbleSort:
    def sort(self, dane):
        wynik = dane.copy()
        n = len(wynik)

        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if wynik[j] > wynik[j + 1]:
                    wynik[j], wynik[j + 1] = wynik[j + 1], wynik[j]
                    swapped = True
            if not swapped:
                break

        return wynik


class SelectionSort:
    def sort(self, dane):
        wynik = dane.copy()
        n = len(wynik)

        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if wynik[j] < wynik[min_idx]:
                    min_idx = j
            wynik[i], wynik[min_idx] = wynik[min_idx], wynik[i]

        return wynik


class InsertionSort:
    def sort(self, dane):
        wynik = dane.copy()

        for i in range(1, len(wynik)):
            key = wynik[i]
            j = i - 1
            while j >= 0 and wynik[j] > key:
                wynik[j + 1] = wynik[j]
                j -= 1
            wynik[j + 1] = key

        return wynik


class MergeSort:
    def sort(self, dane):
        if len(dane) <= 1:
            return dane.copy()

        mid = len(dane) // 2
        left = self.sort(dane[:mid])
        right = self.sort(dane[mid:])

        return self._merge(left, right)

    def _merge(self, left, right):
        wynik = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                wynik.append(left[i])
                i += 1
            else:
                wynik.append(right[j])
                j += 1

        wynik.extend(left[i:])
        wynik.extend(right[j:])
        return wynik


class QuickSort:
    def sort(self, dane):
        if len(dane) <= 1:
            return dane.copy()

        pivot = dane[len(dane) // 2]
        left = [x for x in dane if x < pivot]
        middle = [x for x in dane if x == pivot]
        right = [x for x in dane if x > pivot]

        return self.sort(left) + middle + self.sort(right)


class HeapSort:
    def sort(self, dane):
        wynik = dane.copy()
        n = len(wynik)

        for i in range(n // 2 - 1, -1, -1):
            self._sift_down(wynik, i, n)

        for end in range(n - 1, 0, -1):
            wynik[0], wynik[end] = wynik[end], wynik[0]
            self._sift_down(wynik, 0, end)

        return wynik

    def _sift_down(self, tablica, root, heap_size):
        largest = root
        left = 2 * root + 1
        right = 2 * root + 2

        if left < heap_size and tablica[left] > tablica[largest]:
            largest = left

        if right < heap_size and tablica[right] > tablica[largest]:
            largest = right

        if largest != root:
            tablica[root], tablica[largest] = tablica[largest], tablica[root]
            self._sift_down(tablica, largest, heap_size)


class CountingSort:
    def sort(self, dane):
        if not dane:
            return []

        min_value = min(dane)
        max_value = max(dane)
        counts = [0] * (max_value - min_value + 1)

        for num in dane:
            counts[num - min_value] += 1

        for i in range(1, len(counts)):
            counts[i] += counts[i - 1]

        output = [0] * len(dane)

        for num in reversed(dane):
            index = num - min_value
            counts[index] -= 1
            output[counts[index]] = num

        return output


dane = [-1, 7, 0, -5, 9, 4]

print(BubbleSort().sort(dane))
print(SelectionSort().sort(dane))
print(InsertionSort().sort(dane))
print(MergeSort().sort(dane))
print(QuickSort().sort(dane))
print(HeapSort().sort(dane))
print(CountingSort().sort(dane))
