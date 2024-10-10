# x = int("42")
# y = int(3.1415)
# z = int("hello", base=30)
# print(x, y, z, sep='\n')

import sys
import math
import decimal
import fractions

# STEP = 2 ** 16
# num = 1
# for _ in range(30):
#   print(sys.getsizeof(num), num)
#   num *= STEP


# print(sys.getsizeof(10 ** 100))


# num = 2 ** 16 - 1 
# b = bin(num)
# o = oct(num)
# h = hex(num)
# print(b, o, h)


# pi = 3.141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_375
# print(pi)


# DEFAULT = 42
# num = int(input('Введите уровень или ноль для значения по умолчанию: '))
# level = num or DEFAULT
# print(level)


# data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
# while data:
#   print(data.pop())


# empty_str = ''
# en_str = 'Text'
# ru_str = 'Текст'
# unicode_str = '😀😍😉🙃'
# print(empty_str.__sizeof__())
# print(en_str.__sizeof__())
# print(ru_str.__sizeof__())
# print(unicode_str.__sizeof__())


# print(math.pi, math.e, math.inf, math.nan, math.tau, sep='\n')


# pi = decimal.Decimal('3.141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_375')
# print(pi)
# num = decimal.Decimal(1) / decimal.Decimal(3)
# print(num)


a = complex(2, 3)
b = complex('2+3j')
print(a, b, a == b, sep='\n')