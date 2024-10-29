# Создайте функцию генератор чисел Фибоначчи

def fibonacci_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci_gen()
for _ in range(40):
    print(next(fib_gen))

