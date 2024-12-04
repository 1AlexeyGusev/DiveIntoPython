# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь

class Human:
    def __init__(self, fio, age):
        self.fio = fio
        self._age = age

    def get_age(self):
        return self._age

    def birthday(self):
        self._age += 1

    def full_name(self):
        return f'{self.fio = }'


class Worker(Human):

    def __init__(self, fio, age, user_id):
        super().__init__(fio, age)
        self.user_id = user_id
        if not self.is_valid_id(user_id):
            raise ValueError('Id должен быть шестизначным')

    def is_valid_id(self, user_id):
        id_str = str(user_id)  # Преобразуем в строку для проверки длины и цифр
        return len(id_str) == 6 and id_str.isdigit()

    @property
    def access_level(self):
        return sum(int(digit) for digit in str(self.user_id)) % 7


if __name__ == '__main__':
    worker = Worker('Alex Ovechkin', 39, 111411)
    print(worker.full_name())
    print(worker.get_age())
    print(worker.user_id)
    print(worker.access_level)
