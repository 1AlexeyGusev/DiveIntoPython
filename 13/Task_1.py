# Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# Обрабатывайте не числовые данные как исключения.

def get_num() -> int | float:
    while True:
        num = input("Введите число: ")
        try:
            n = float(num)
            if n.is_integer():
                return int(n)
            return n
        except ValueError as e:
            print("Введены не числовые данные")


if __name__ == '__main__':
    print(get_num())

