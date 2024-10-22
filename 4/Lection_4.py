# a = 42
# print(type(a), id(a))
# print(type(id))

#
# very_bad_programming_style = sum
# print(very_bad_programming_style([1, 2, 3]))


# def quadratic_equations(a: int | float, b: int | float, c: int |
# float) -> tuple[float, float] | float | str:
#     d = b ** 2 - 4 * a * c
#     if d > 0:
#         return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
#     elif d == 0:
#         return -b / (2 * a)
#     else:
#         return 'Нет решений'
# print(quadratic_equations(2, -3, -9))


# def no_mutable(a: int) -> int:
#   a += 1
#   print(f'In func {a = }') # Для демонстрации работы, но не для привычки принтить из функции
#   return a
# a = 42
# print(f'In main {a = }')
# z = no_mutable(a)
# print(f'{a = }\t{z = }')


# def mutable(data: list[int]) -> list[int]:
#     for i, item in enumerate(data):
#         data[i] = item + 1
#     print(f'In func {data = }') # Для демонстрации работы, но не для привычки принтить из функции
#     return data
# my_list = [2, 4, 6, 8]
# print(f'In main {my_list = }')
# new_list = mutable(my_list)
# print(f'{my_list = }\t{new_list = }')


# def no_return(data: list[int]):
#   for i, item in enumerate(data):
#     data[i] = item + 1
#     print(f'In func {data = }') # Для демонстрации работы, но не для привычки принтить из функции
# my_list = [2, 4, 6, 8]
# print(f'In main {my_list = }')
# new_list = no_return(my_list)
# print(f'{my_list = }\t{new_list = }')


# def from_one_to_n(n, data=[]):
#   for i in range(1, n + 1):
#     data.append(i)
#     return data
# new_list = from_one_to_n(5)
# print(f'{new_list = }')
# other_list = from_one_to_n(7)
# print(f'{other_list = }')


# def standard_arg(arg):
#   print(arg) # Принтим для примера, а не для привычки
# standard_arg(42)
# standard_arg(arg=42)


# def pos_only_arg(arg, /):
#   print(arg) # Принтим для примера, а не для привычки
# pos_only_arg(42)
# pos_only_arg(arg=42) # TypeError: pos_only_arg() got some positional-only
# arguments passed as keyword arguments: 'arg'


# def func(y: int) -> int:
#   x = 100
#   print(f'In func {x = }') # Для демонстрации работы, но не для привычки принтить из функции
#   return y + 1
# x = 42
# print(f'In main {x = }')
# z = func(x)
# print(f'{x = }\t{z = }')


# def main(a):
#     x = 1
#     def func(y):
#         nonlocal x
#         x += 100
#         print(f'In func {x = }') # Для демонстрации работы, но не для привычки принтить из функции
#         return y + 1
#     return x + func(a)
# x = 42
# print(f'In main {x = }')
# z = main(x)
# print(f'{x = }\t{z = }')


my_dict = {'two': 2, 'one': 1, 'four': 4, 'three': 3, 'ten': 10}
s_key = sorted(my_dict.items())
s_value = sorted(my_dict.items(), key=lambda x: x[1])
print(f'{s_key = }\n{s_value = }')