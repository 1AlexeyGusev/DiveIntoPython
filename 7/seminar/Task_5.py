# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

from random import randint, choices
from string import ascii_lowercase, digits


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

def gen_files(**kwargs) -> None:
    for ext, count in kwargs.items():
        create_files(extension=ext, files_num=count)


if __name__ == '__main__':
    gen_files(jpg=2, txt=1)