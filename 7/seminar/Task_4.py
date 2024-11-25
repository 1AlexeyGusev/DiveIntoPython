# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

from random import randint, choices
from string import ascii_lowercase, digits, punctuation


def create_files(
        extension: str='bin',
        name_min_len=6,
        name_max_len=30,
        file_size_min=256,
        file_size_max=4096,
        files_num=2
) -> None:
    for _ in range(files_num):
        name = ''.join(choices(ascii_lowercase + digits + '_',
                               k=randint(name_min_len, name_max_len))) + extension
        data = bytes(randint(0,255) for _ in range(randint(file_size_min, file_size_max)))
        with open(f'{name}.{extension}', 'wb') as file:
            file.write(data)

create_files()