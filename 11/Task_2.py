# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра


class Archive:
    # Классовые списки для хранения архивов
    archive_nums = []
    archive_str = []

    def __init__(self, num, string):
        # Сохраняем переданные данные
        self.num = num
        self.string = string

        # Добавляем данные в архивы
        Archive.archive_nums.append(num)
        Archive.archive_str.append(string)

    def __repr__(self):
        return f'Архив(число={self.num}, строка="{self.string}")'

    def repr_for_user(self):
        # Представление для пользователя
        return f'Число: {self.num}, Строка: "{self.string}"'

    @classmethod
    def get_archive(cls):
        return cls.archive_nums, cls.archive_str


# Пример использования
archive1 = Archive(42, "Привет")
archive2 = Archive(100, "Мир")

print(archive1)  # Архив(число=42, строка="Привет")
print(archive2)  # Архив(число=100, строка="Мир")

# Получаем архивы
nums, strings = Archive.get_archive()
print("Архив чисел:", nums)  # Архив чисел: [42, 100]
print("Архив строк:", strings)  # Архив строк: ['Привет', 'Мир']
