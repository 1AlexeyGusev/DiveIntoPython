# Задание №4
# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

# 1--------------------------------------------------------------

data = [42, 73, 5, 42, 42, 2, 3, 7, 73, 42]

data = [item for item in data if data.count(item) != 2]
print(data)

# 2----------------------------------------------------------------

data1 = [42, 73, 5, 42, 42, 2, 3, 7, 73, 42]
unique_list = []
for item in data1:
    if data1.count(item) != 2:
        unique_list.append(item)
print(unique_list)

# 3---------------------------------------------------------------

data2 = [42, 73, 5, 42, 42, 2, 3, 7, 73, 42]
COUNT = 2
for item in set(data2):
    if data2.count(item) == COUNT:
        for _ in range(COUNT):
            data2.remove(item)
print(data2)
