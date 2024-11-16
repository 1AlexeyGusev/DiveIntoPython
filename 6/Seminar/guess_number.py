# Улучшаем задачу 2.
# � Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# � Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# � Для преобразования строковых аргументов командной
# строки в числовые параметры используйте генераторное выражение.

__all__ = ['guessing']
from random import randint
from sys import argv


def guessing(lower_num: int = 0, upper_num: int = 100, count: int = 10) -> bool:
    number = randint(lower_num, upper_num)
    for _ in range(count):
        answer = int(input("Input number: "))
        if answer == number:
            return True
        elif answer > number:
            print(f'Число {answer} больше загаданного')
        else:
            print(f'Число {answer} меньше загаданного')

if __name__ == '__main__':
    params = argv[1:]
    params = (int(number) for number in params)
    print(guessing(*params))