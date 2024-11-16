# Создайте модуль с функцией внутри.
# � Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# � Внутри генерируется случайное число в указанных границах и пользователь должен угадать его
# за заданное число попыток.
# � Функция выводит подсказки “больше” и “меньше”.
# � Если число угадано, возвращается истина, а если попытки
# исчерпаны - ложь.

from random import randint


def guessing(lower_num: int = 0, upper_num: int = 100, count: int = 10) -> bool:
    number = randint(lower_num, upper_num)
    for _ in range(count):
        answer = int(input("Input number"))
        if answer == number:
            return True
        elif answer > number:
            print(f'Число {answer} больше загаданного')
        else:
            print(f'Число {answer} меньше загаданного')

if __name__ == '__main__':
    print(guessing())