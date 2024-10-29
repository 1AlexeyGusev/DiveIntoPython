# ✔ Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного генератора, где каждый элемент генератора —
# отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт» без перехода на новую строку.

LOW_LIMIT = 2
HIGH_LIMIT = 10
COLUMN = 4

table = (
    f'{multiply_1:>2} * {multiply_2:>2} = {multiply_1 * multiply_2:>2}\t' if multiply_1 != row+COLUMN-1 else
    f'{multiply_1:>2} * {multiply_2:>2} = {multiply_1 * multiply_2:>2}\n' if multiply_2 != HIGH_LIMIT else
    f'{multiply_1:>2} * {multiply_2:>2} = {multiply_1 * multiply_2:>2}\n\n'
    for row in(LOW_LIMIT, LOW_LIMIT+COLUMN)
    for multiply_2 in range(LOW_LIMIT, HIGH_LIMIT+1)
    for multiply_1 in range(row, row+COLUMN)
)
print(*table)