# Вспоминаем задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя
# информацию в JSON файл.
# Напишите класс пользователя, который хранит эти данные в
# свойствах экземпляра.
# Отдельно напишите функцию, которая считывает информацию
# из JSON файла и формирует множество пользователей.

import json
import os
from pathlib import Path


class User:
    def __init__(self, name, user_id, access_level):
        self.name = name
        self.user_id = user_id
        self.access_level = access_level

    def __str__(self):
        return f'Пользователь: {self.name}\n' \
               f'ID: {self.user_id}\n' \
               f'Уровень доступа: {self.access_level}'


def read_file(file: Path) -> set:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            read_json = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f'Ошибка при чтении файла: {e}')
        return set()

    users = set()
    for access_level, value_dict in read_json.items():
        for user_id, name in value_dict.items():
            users.add(User(name, user_id, access_level))

        return users


if __name__ == '__main__':
    file_path = Path(r'D:\обучение\Погружение в Python\8\seminar\users.json')
    users = read_file(file_path)
    for user in users:
        print(user)
