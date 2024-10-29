# Напишите программу, которая выводит на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.

LOW_LIMIT = 1
HIGH_LIMIT = 100
DIV_3 = 3
DIV_5 = 5
# for num in range(LOW_LIMIT, HIGH_LIMIT + 1):
#     if num % (DIV_3 * DIV_5) == 0:
#         print('FizzBuzz')
#     elif num % DIV_3 == 0:
#         print('Fizz')
#     elif num % DIV_5 == 0:
#         print('Buzz')
#     else:
#         print(num)

print(*(
'FizzBuzz' if num % (DIV_3 * DIV_5) == 0 else
'Fizz' if num % DIV_3 == 0 else
'Buzz' if num % DIV_5 == 0
else num for num in range(LOW_LIMIT, HIGH_LIMIT + 1)
), sep=', ')