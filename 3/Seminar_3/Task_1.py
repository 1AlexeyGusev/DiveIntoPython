# Задание №1
# ✔ Вручную создайте список с целыми числами, которые
# повторяются. Получите новый список, который содержит
# уникальные (без повтора) элементы исходного списка.
# ✔ *Подготовьте два решения, короткое и длинное, которое
# не использует другие коллекции помимо списков.

data = [42, 73, 5, 42, 42, 2, 3, 7, 73, 42]
print(list(set(data)))

new_list = []
for item in data:
    if item not in new_list:
        new_list.append(item)
print(new_list)

new_list_1 = sorted(data)
for i in range(len(new_list_1)-1,0,-1):
    if new_list_1[i] == new_list_1[i-1]:
        del new_list_1[i]
print(new_list_1)


