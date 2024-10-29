# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

def parse_file_path(file_path):
    # Находим последний слэш для извлечения пути
    last_slash_index = file_path.rfind('/')
    if last_slash_index == -1:
        directory = ''
        file_name = file_path
    else:
        directory = file_path[:last_slash_index]
        file_name = file_path[last_slash_index + 1:]

    # Находим точку для извлечения имени файла и расширения
    last_dot_index = file_name.rfind('.')
    if last_dot_index == -1:
        name = file_name
        extension = ''
    else:
        name = file_name[:last_dot_index]
        extension = file_name[last_dot_index:]

    return (directory, name, extension)

# Пример использования
absolute_path = "/home/user/documents/file.txt"
result = parse_file_path(absolute_path)
print(result)