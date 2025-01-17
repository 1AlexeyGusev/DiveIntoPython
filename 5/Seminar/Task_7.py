# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел, начиная с числа 2.
# ✔ Для проверки числа на простоту используйте правило: «число является простым, если делится
# нацело только на единицу и на себя».

def is_prime(num):
    prime_num = 2
    count = 1
    yield prime_num
    prime_num += 1
    while count < num:
        for div in range(3, int(prime_num/2), 2):
            if prime_num % div == 0:
                break
        else:
            count += 1
            yield prime_num
        prime_num += 2

print(*(is_prime(50)))