# Добавьте в модуль с загадками функцию, которая хранит
# словарь списков.
# � Ключ словаря - загадка, значение - список с отгадками.
# � Функция в цикле вызывает загадывающую функцию, чтобы
# передать ей все свои загадки.

def puzzle(emigma: str, answers: list[str], count: int = 3) -> int:
    print(f'Отгадай загадку: {emigma}')
    for i in range(1, count + 1):
        answer = input(f"Попытка номер {i}, Твой ответ: ")
        if answer in answers:
            return i
    return 0


def storage():
    puzzles = {
        "Зимой и летом - одним цветом": ["ель", "сосна", "елка"],
        "Сидит дед - во сто шуб одет": ["лук", "чеснок", "дед"],
        "Висит груша - нельзя скушать": ["груша", "лампа", "лампочка"]
    }
    # print(puzzles.items())
    for key, value in puzzles.items():
        # print(key, value)
        res = puzzle(key, value)
        print(f'Угадал с {res} попытки' if res else 'Не угадал')


if __name__ == '__main__':
    storage()
    # res = puzzle('Зимой и летом одним цветом', ["елка", "доллар", "ель"])
    # print(f'Угадал с {res} попытки' if res else 'Не угадал')
