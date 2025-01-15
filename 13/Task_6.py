# Доработайте классы исключения так, чтобы они выдали
# подробную информацию об ошибках.
# Передавайте необходимые данные из основного кода проекта.

import json
from pathlib import Path


class UserException(Exception):
    def __init__(self, message, user_id=None, name=None):
        super().__init__(message)
        self.user_id = user_id
        self.name = name

    def __str__(self):
        if self.user_id and self.name:
            return f'{self.__class__.__name__}: {self.args[0]} (ID: {self.user_id}, Имя: {self.name})'
        return f'{self.__class__.__name__}: {self.args[0]}'

class LevelError(UserException):


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

        raise AccessException(f'Пользователь не найден.', user_id=user_id, name=name)

    def add_user(self, new_user: User, current_user: User):
        """Добавляет нового пользователя, если уровень доступа позволяет."""
        if new_user.access_level < current_user.access_level:
            raise LevelError(f'Уровень доступа нового пользователя ниже, чем у текущего.')

        self.users.add(new_user)
        print(f'Пользователь {new_user.name} успешно добавлен.')