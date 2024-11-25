# ✔ Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл

import random
from pathlib import Path

VOWELS = 'eyuioa'
CONSONANTS = 'qwrtpsdfghjklzxcvbnm'
MIN_LEN = 4
MAX_LEN = 7

# 1 способ
# def generate_name(count: int, file_name: str | Path) -> None:
#     for _ in range(count):
#         first_chr = random.choice([-1, 1])
#         name = ''
#         for _ in range(random.randint(MIN_LEN, MAX_LEN)):
#             if first_chr == -1:
#                 name += random.choice(CONSONANTS)
#             else:
#                 name += random.choice(VOWELS)
#             first_chr *= -1
#
#         with open(file_name, 'a', encoding='UTF-8') as f:
#             f.write(name.title() + '\n')


#2 способ

from random import choice, randint

def generate_name(count: int, file_name: str | Path) -> None:
    for _ in range(count):
        name = ''.join(choice(VOWELS) if i in(1,4,6) else choice(CONSONANTS)
            for i in range(randint(MIN_LEN, MAX_LEN)))

        with open(file_name, 'a', encoding='UTF-8') as f:
            f.write(name.title() + '\n')


generate_name(10, 'generate_name.txt')

