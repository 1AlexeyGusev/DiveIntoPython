# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# ✔ При достижении конца более короткого файла, возвращайтесь в его начало.

from typing import TextIO


def read_or_begin(file_descriptor: TextIO) -> str:
    text = file_descriptor.readline()
    if text == '':
        file_descriptor.seek(0)
        text = file_descriptor.readline()
    return text.strip()


def convert(numbers: str, names: str, result: str) -> None:
    with(
        open(numbers, 'r', encoding='utf-8') as f_numbers,
        open(names, 'r', encoding='utf-8') as f_names,
        open(result, 'w', encoding='utf-8') as f_result
    ):
        len_names = sum(1 for _ in f_names)
        len_numbers = sum(1 for _ in f_numbers)
        for _ in range(max(len_names, len_numbers)):
            nums_str = read_or_begin(f_numbers)
            name = read_or_begin(f_names)
            num_i, num_f = nums_str.split('|')
            mult = int(num_i) * float(num_f)
            if mult < 0:
                f_result.write(f'{name.lower()} {-mult} \n')
            else:
                f_result.write(f'{name.upper()} {mult} \n')

convert('random_numbers.txt', 'generate_name.txt', 'result.txt')
