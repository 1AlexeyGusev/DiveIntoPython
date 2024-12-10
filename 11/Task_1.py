# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания (time.time)


import time

class MyString(str):
    def __new__(cls, content, author):
        # Создаем новый экземпляр строки
        instance = super().__new__(cls, content)
        # Сохраняем имя автора и время создания
        instance.author = author
        instance.creation_time = time.time()
        return instance

    def __init__(self, content, author):
        # Инициализация не требуется, так как все уже сделано в __new__
        pass

    def __repr__(self):
        # Переопределяем метод для удобного отображения
        return f'МояСтрока("{self}", автор="{self.author}", время создания={self.creation_time})'

if __name__ == '__main__':
    # Пример использования
    string = MyString("Привет, мир!", "Иван")
    print(string)
    print(f"Автор: {string.author}")
    print(f"Время создания: {string.creation_time}")