# Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

def fix_unicode(text: str) -> list[int]:
    result = []
    for char in set(text):
        result.append(ord(char))
    return sorted(result, reverse=True)

string = input('Введите строку: ')
print(fix_unicode(string))

