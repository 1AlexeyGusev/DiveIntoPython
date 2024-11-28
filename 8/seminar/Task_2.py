# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# При перезапуске функции уже записанные в файл данные должны сохраняться.

# import json
# from pathlib import Path
#
#
# def set_users(user_file: Path) -> None:
#     unique_id = set()
#     if not user_file.is_file():
#         data = {str(i): {} for i in range(1, 7 + 1)}
#     else:
#         with open(user_file, 'r') as file:
#             data = json.load(file)

import json
import os


def save_data(data, filename='users.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def load_data(filename='users.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return {}


def main():
    filename = 'users.json'
    users_data = load_data(filename)

    while True:
        name = input("Введите имя: ")
        user_id = input("Введите личный идентификатор: ")

        # Проверка уникальности идентификатора
        if any(user_id in users for users in users_data.values()):
            print("Ошибка: идентификатор должен быть уникальным.")
            continue

        access_level = input("Введите уровень доступа (от 1 до 7): ")

        if access_level not in map(str, range(1, 8)):
            print("Ошибка: уровень доступа должен быть от 1 до 7.")
            continue

        # Добавление пользователя в соответствующий уровень доступа
        if access_level not in users_data:
            users_data[access_level] = {}

        users_data[access_level][user_id] = name

        save_data(users_data, filename)
        print("Данные успешно сохранены.")


if __name__ == "__main__":
    save_data(main())

