# ✔ Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку

even_num = (number for number in range(0, 101, 2) if number % 10 + number // 10 != 8)
print(*even_num)
