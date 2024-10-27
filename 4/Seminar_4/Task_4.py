# Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.

def bubble_sort(arr):
    for i in range(len(arr)):
        swapped = True
        for j in range(0, len(arr) - i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = False
        if swapped:
            return arr

data = [73,42,7, 3, 5, 2,11]
print('Отсортированный список', bubble_sort(data))