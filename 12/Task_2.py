# Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.

from  collections import deque
import json
import time
from pathlib import Path

class FactorialCalc:

    def __init__(self, k):
        self.memory = deque(maxlen=k)

    def __call__(self, n, *args, **kwargs):
        # Проверка на неотрицательное целое число
        if n < 0:
            raise ValueError("Факториал не определен для отрицательных чисел.")
        res = 1
        for num in range(2, n+1):
            res *= num
        self.memory.append({n: res})

        return self.memory[-1]
    def old(self):
        return self.memory

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        dump_dict = {}
        while self.memory:
            dump_dict.update(self.memory.popleft())
            # Сохраняем в JSON файл с текущим временем в имени
        filename = f'{int(time.time())}.json'
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(dump_dict, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    with FactorialCalc(5) as factorial_calculator:
        print(factorial_calculator(5))  # Вычисляет 5!
        print(factorial_calculator(3))  # Вычисляет 3!
        print(factorial_calculator(4))  # Вычисляет 4!