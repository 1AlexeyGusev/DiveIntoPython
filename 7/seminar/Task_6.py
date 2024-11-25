# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.


from random import randint, choices
from string import ascii_lowercase, digits
from pathlib import Path
from os import chdir


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

def gen_files(path: str | Path, **kwargs) -> None:
    if isinstance(path, str):
        path = Path(path)
    if not path.is_dir():
        path.mkdir(parents=True)
    chdir(path)

    for ext, count in kwargs.items():
        create_files(extension=ext, files_num=count)


if __name__ == '__main__':
    gen_files('D:\\обучение\\Погружение в Python\\7\\seminar\\new', jpg=2, txt=1)