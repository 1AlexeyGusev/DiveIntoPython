# Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.

def num1_num2(string: str) -> dict[str, int]:
    num1, num2 = map(int, string.split())
    result = {}
    for code in range(min(num1, num2), max(num1, num2) + 1):
        result[chr(code)] = code

    return result

print(num1_num2('12 46'))

