# � Добавьте в модуль с загадками функцию, которая
# принимает на вход строку (текст загадки) и число (номер попытки, с которой она угадана).
# � Функция формирует словарь с информацией о результатах отгадывания.
# � Для хранения используйте защищённый словарь уровня модуля.
# � Отдельно напишите функцию, которая выводит результаты
# угадывания из защищённого словаря в удобном для чтения виде.
# � Для формирования результатов используйте генераторное выражение.

__all__ = ['save_puzzle', 'puzzle','show','storage']
_data = {}


def save_puzzle(enigma: str, count: int) -> None:
    _data.update({enigma: count})


def puzzle(enigma: str, answers: list[str], count: int = 3) -> int:
    print(f'Отгадай загадку: {enigma}')
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
        save_puzzle(key, res)
        # print(_data)


def show():
    res = (
        f'Загадку {enigma} угадал с {count}-й попытки' if count
        else f'Загадку {enigma} не угадал'
        for enigma, count in _data.items()
    )
    print(*res, sep="\n")

if __name__ == '__main__':
    storage()
    print()
    show()
    # res = puzzle('Зимой и летом одним цветом', ["елка", "доллар", "ель"])
    # print(f'Угадал с {res} попытки' if res else 'Не угадал')
