# Доработаем задачи 3 и 4. Создайте класс проекта, который
# имеет следующие методы:
# загрузка данных (функция из задания 4)
# вход в систему - требует указать имя и id пользователя. Для
# проверки наличия пользователя в множестве используйте
# магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение
# доступа. А если пользователь есть, получите его уровень из
# множества пользователей.
# добавление пользователя. Если уровень пользователя
# меньше, чем ваш уровень, вызывайте исключение уровня
# доступа.


import json
from pathlib import Path


class UserException(Exception):
    pass

class LevelError(UserException):
    pass

class AccessException(UserException):
    pass


class User:
    def __init__(self, name, user_id, access_level):
        self.name = name
        self.user_id = user_id
        self.access_level = access_level

    def __str__(self):
        return f'Пользователь: {self.name}\n' \
               f'ID: {self.user_id}\n' \
               f'Уровень доступа: {self.access_level}'

    def __eq__(self, other):
        return self.name == other.name and self.user_id == other.user_id


class Repo:

    def __init__(self):
        self.user = None
        self.users = set()

    def read_file(self, file: Path) -> set:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                read_json = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f'Ошибка при чтении файла: {e}')
            return set()

        for access_level, value_dict in read_json.items():
            for user_id, name in value_dict.items():
                self.users.add(User(name, user_id, access_level))

            return self.users

    def login(self, name: str, user_id: str) -> str:
        """Проверяет наличие пользователя и возвращает его уровень доступа."""
        user_to_check = User(name, user_id, None)  # Уровень доступа не важен для проверки
        for user in self.users:
            if user == user_to_check:
                return f'Уровень доступа пользователя {name}: {user.access_level}'

        raise AccessException(f'Пользователь с ID {user_id} и именем {name} не найден.')

    def add_user(self, new_user: User, current_user: User):
        """Добавляет нового пользователя, если уровень доступа позволяет."""
        if new_user.access_level < current_user.access_level:
            raise LevelError(f'Уровень доступа нового пользователя {new_user.name} ниже, чем у {current_user.name}.')

        self.users.add(new_user)
        print(f'Пользователь {new_user.name} успешно добавлен.')




