# data = ["один", "два", "три", "четыре", "пять", "шесть", "семь",]
# a, b, c, *d = data
# print(f'{a=} {b=} {c=} {d=}')
# a, b, *c, d = data
# print(f'{a=} {b=} {c=} {d=}')
# a, *b, c, d = data
# print(f'{a=} {b=} {c=} {d=}')
# *a, b, c, d = data
# print(f'{a=} {b=} {c=} {d=}')


# a = b = c = 0
# a += 42
# print(f'{a=} {b=} {c=}')


# a = b = c = {1, 2, 3}
# a.add(42)
# print(f'{a=} {b=} {c=}')

#
# t = 1, 2, 3
# print(f'{t=}, {type(t)}')

#
# a = b = c = 42
# # if a == b and b == c:
# if a == b == c:
#   print('Полное совпадение')


# a = 12; b = 42; c = 73
# if a < b < c: b = None; print('Ужасный код')


# data = {10, 9, 8, 1, 6, 3}
# a, b, c, *d, e = data
# print(a, b, c, d, e)


# data = [2, 4, 6, 8]
# list_iter = iter(data)
# print(list_iter)


# data = [2, 4, 6, 8]
# list_iter = iter(data)
# print(*list_iter)


# data = [2, 4, 6, 8]
# list_iter = iter(data)
# print(next(list_iter, 42))
# print(next(list_iter, 42))
# print(next(list_iter, 42))
# print(next(list_iter, 42))
# print(next(list_iter, 42))
# print(next(list_iter, 42))


# data = {"один": 1, "два": 2, "три": 3}
# x = iter(data.items())
# print(x)
# y = next(x)
# print(y)
# z = next(iter(y))
# print(z)
#
# a = range(0, 10, 2)
# print(f'{a=}, {type(a)=}, {a.__sizeof__()=}, {len(a)}')
# b = range(-1_000_000, 1_000_000, 2)
# print(f'{b=}, {type(b)=}, {b.__sizeof__()=}, {len(b)}')

#
# x = [1, 1, 2, 3, 5, 8, 13]
# y = [1, 2, 6, 24, 120, 720]
# print(f'{len(x)=}\t{len(y)=}')
# mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)
# res = list(mult)
# print(f'{len(res)=}\n{res}')


# data = {2, 4, 4, 6, 8, 10, 12}
# res1 = {None: item for item in data if item > 4}
# res2 = (item for item in data if item > 4)
# res3 = [[item] for item in data if item > 4]
# print(res1, res2, res3)


# def factorial(n):
#     number = 1
#     for i in range(1, n + 1):
#         number *= i
#         yield number
#     for i, num in enumerate(factorial(10), start=1):
#         print(f'{i}! = {num}')
#
#
# print(factorial(10))


def gen(a: int, b: int) -> str:
    if a > b:
        a, b = b, a
    for i in range(a, b + 1):
        yield str(i)
for item in gen(10, 1):
    print(f'{item = }')
