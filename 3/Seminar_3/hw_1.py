# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.

elements = [1, 2, 3, 2, 4, 3, 5, 1, 6]
seen = set()
result = set()
for el in elements:
    if el in seen:
        result.add(el)
    else:
        seen.add(el)
print(list(result))
