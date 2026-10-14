def bubble_sort(lista):
    n = len(lista)
    for i in range(0,n,1):
        for j in range(0, n-i-1, 1):
            if (lista[j]>lista[j+1]):
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp
    return lista

def bubble_sort_statystyki(lista):
    przyrownania = 0
    zamiany = 0
    n = len(lista)
    for i in range(0, n, 1):
        for j in range(0, n - i - 1, 1):
            przyrownania = przyrownania + 1
            if (lista[j] > lista[j + 1]):
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp
                zamiany = zamiany + 1
    return lista, f'Liczba zmian: {zamiany}', f'Liczba przyrównań: {przyrownania}'

def bubble_sort_optymalny(lista):
    przyrownania = 0
    zamiany = 0
    n = len(lista)
    for i in range(0, n, 1):
        byla_zamiana = False
        for j in range(0, n - i - 1, 1):
            przyrownania = przyrownania + 1
            if (lista[j] > lista[j + 1]):
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp
                zamiany = zamiany + 1
                byla_zamiana = True
        if not byla_zamiana:
            break
    return lista, f'Liczba zmian: {zamiany}', f'Liczba przyrównań: {przyrownania}'

if __name__ == '__main__':

    print("Ćwiczenie 3 - implementacja bubble sort")
lista_list = [[5, 2, 8, 1, 4], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1],
              [10], [], [3, 3, 2, 1, 2]]
for element in lista_list:
    print("Przed:", element, "  Po sortowaniu:", bubble_sort(element.copy()))
print()

print("Ćwiczenie 4 - implementacja bubble sort ze statystykami")
lista_list_2 = [[1, 2, 3, 4, 5],[5, 4, 3, 2, 1],[3, 1, 4, 2, 5]]
for element in lista_list_2:
    print(element, bubble_sort_statystyki(element.copy()))
print()

print("Ćwiczenie 5 - implementacja bubble sort z optymalizacją")
for element in lista_list_2:
    print("Przed:", element, "Po zoptymalizowanym sortowaniu:", bubble_sort_optymalny(element.copy()))
