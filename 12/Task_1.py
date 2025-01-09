# Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.



"""
                                        1 вариант из chatGPT Monica
"""

# class FactorialCalculator:
#     def __init__(self, k):
#         self.k = k
#         self.history = []
#
#     def __call__(self, n):
#         if n < 0:
#             raise ValueError("Факториал не определён для отрицательных чисел.")
#         result = self.factorial(n)
#         self.store_history(n, result)
#         return result
#
#     def factorial(self, n):
#         if n == 0 or n == 1:
#             return 1
#         return n * self.factorial(n - 1)
#
#     def store_history(self, n, result):
#         self.history.append((n, result))
#         if len(self.history) > self.k:
#             self.history.pop(0)  # Удаляем самое старое значение, если превышен лимит
#
#     def get_history(self):
#         return self.history
#
# # Пример использования
# calc = FactorialCalculator(5)
# print(calc(5))  # 120
# print(calc(4))  # 24
# print(calc(3))  # 6
# print(calc.get_history())  # [(5, 120), (4, 24), (3, 6)]

"""
                                                                  2 вариант из семинара
"""

from  collections import deque

class FactorialCalc:

    def __init__(self, k):
        self.memory = deque(maxlen=k)

    def __call__(self, n, *args, **kwargs):
        res = 1
        for num in range(2, n+1):
            res *= num
        self.memory.append({n: res})

        return self.memory[-1]
    def old(self):
        return self.memory

f = FactorialCalc(5)
for i in range(2, 10):
    print(f(i))
    print(f.old())


