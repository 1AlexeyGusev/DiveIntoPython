# a = 42
# b = 'Hello world!'
# c = [1, 3, 5, 7]
# my_list = [None]
# my_list.append(a)
# print(my_list)
# my_list.append(b)
# print(my_list)
# my_list.append(c)
# print(my_list)


# a = 42
# b = 'Hello world!'
# c = [1, 3, 5, 7]
# my_list = [None]
# # my_list.extend(a) # TypeError: 'int' object is not iterable
# print(my_list)
# my_list.extend(b)
# print(my_list)
# my_list.extend(c)
# print(my_list)
# my_list.extend(my_list)
# print(my_list)


# my_list = [2, 4, 6, 8, 10, 12]
# spam = my_list.pop()
# print(spam, my_list)
# eggs = my_list.pop(1)
# print(eggs, my_list)
# err = my_list.pop(10) # IndexError: pop index out of range


# my_list = [2, 4, 6, 2, 8, 10, 12, 2, 4, 14, 2]
# spam = my_list.count(2)
# print(spam)
# eggs = my_list.count(3)
# print(eggs)


# my_list = [2, 4, 6, 2, 8, 10, 12, 2, 4, 14, 2]
# spam = my_list.index(4)
# print(spam)
# eggs = my_list.index(4, spam + 1, 90)
# print(eggs)
# err = my_list.index(3) # ValueError: 3 is not in list


# my_list = [2, 4, 6, 8, 10, 12]
# my_list.insert(2, 555)
# print(my_list)
# my_list.insert(-2, 13)
# print(my_list)
# my_list.insert(42, 73) # my_list.append(73)
# print(my_list)


# my_list = [4, 8, 2, 9, 1, 7, 2]
# sort_list = sorted(my_list)
# print(my_list, sort_list, sep='\n')
# rev_list = sorted(my_list, reverse=True)
# print(my_list, rev_list, sep='\n')


# my_list = [4, 8, 2, 9, 1, 7, 2]
# res = reversed(my_list)
# print(type(res), res)
# rev_list = list(reversed(my_list))
# print(rev_list)


# my_list = [4, 8, 2, 9, 1, 7, 2]
# new_list = my_list[::-1]
# print(my_list, new_list, sep='\n')

# my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
# print(my_list[2:7:2])
# print(my_list[:7:2])
# print(my_list[2::2])
# print(my_list[2:7:])
# print(my_list[8:3:-1])
# print(my_list[3::])
# print(my_list[:7:])

#
# my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
# new_list = my_list
# print(my_list, new_list, sep='\n')
# my_list[2] = 555
# print(my_list, new_list, sep='\n')

#
# my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
# new_list = my_list.copy()
# print(my_list, new_list, sep='\n')
# my_list[2] = 555
# print(my_list, new_list, sep='\n')


# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# new_m = matrix.copy()
# print(matrix, new_m, sep='\n')
# matrix[0][1] = 555
# print(matrix, new_m, sep='\n')


# import copy
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# new_m = copy.deepcopy(matrix)
# print(matrix, new_m, sep='\n')
# matrix[0][1] = 555
# print(matrix, new_m, sep='\n')


# my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# print(len(my_list))    #10
# print(len(matrix))    #3
# print(len(matrix[1]))    #4


# my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
# print(my_list[2:6:2])
# print(my_list.pop())
# print(my_list.extend([314, 42]))
# print(my_list.sort(reverse=False))
# print(my_list)


# text = 'Hello world!'
# print(text[6])
# print(text[3:7])
# new_txt = text.replace('l', 'L', 2)
# print(text, new_txt, sep='\n')


# text = 'Hello world!'
# print(text.count('l'))
# print(text.index('l'))
# print(text.find('l'))
# print(text.find('z'))

# pi = 3.1415
# print(f'Число Пи с точностью два знака: {pi:.2f}')
# data = [3254, 4364314532, 43465474, 2342, 462256, 1747]
# for item in data:
#   print(f'{item:>10}')
# num = 2 * pi * data[1]
# print(f'{num = :_}')


# link = 'https://habr.com/ru/users/dzhoker1/posts/'
# urls = link.split('/')
# print(urls)
# a, b, c = input('Введите 3 числа через пробел: ').split()
# print(c, b, a)

#
# text = 'однажды в СТУДЁНУЮ зИмнЮЮ ПоРУ'
# print(text.upper())
# print(text.lower())
# print(text.title())
# print(text.capitalize())


# a = ()
# b1 = 1,
# b2 = (1,)
# c1 = 1, 2, 3,
# c2 = (1, 2, 3)
# d = tuple(range(3))
# print(a, b1, b2, c1, c2, d, sep='\n')


# my_tuple = (2, 4, 6, 2, 8, 10, 12, 14, 16, 18)
# print(my_tuple[2:6:2])
# print(my_tuple[-3])
# print(my_tuple.count(2))
# print(f'{my_tuple = }')
# print(my_tuple.index(2, 2))
# print(type('text',))

# a = {'one': 42, 'two': 3.14, 'ten': 'Hello world!'}
# b = dict(one=42, two=3.14, ten='Hello world!')
# c = dict([('one', 42), ('two', 3.14), ('ten', 'Hello world!')])
# print(a == b == c)


# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
# my_dict['ten'] = 10
# print(my_dict)


# TEN = 'ten'
# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# print(my_dict['two'])
# print(my_dict[TEN])
# print(my_dict[1]) # KeyError: 1


# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# print(my_dict.get('two'))
# print(my_dict.get('five'))
# print(my_dict.get('five', 5))
# print(my_dict.get('ten', 5))


my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.setdefault('five')
print(f'{spam = }\t{my_dict=}')
eggs = my_dict.setdefault('six', 6)
print(f'{eggs = }\t{my_dict=}')
new_spam = my_dict.setdefault('two')
print(f'{new_spam=}\t{my_dict=}')
new_eggs = my_dict.setdefault('one', 1_000)
print(f'{new_eggs=}\t{my_dict=}')

#
# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# print(my_dict.keys())
# for key in my_dict.keys():
#     print(key)
#
#
# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# print(my_dict.values())
# for value in my_dict.values():
#     print(value)


# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# print(my_dict.items())
# for tuple_data in my_dict.items():
#     print(tuple_data)
# for key, value in my_dict.items():
#     print(f'{key = } value before 100 - {100 - value}')

#
# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# spam = my_dict.popitem()
# print(f'{spam = }\t{my_dict=}')
# eggs = my_dict.popitem()
# print(f'{eggs = }\t{my_dict=}')


# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# my_dict.update(dict(six=6))
# print(my_dict)
# my_dict.update(dict([('five', 5), ('two', 42)]))
# print(my_dict)


# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# print(my_dict.setdefault('ten', 555))
# print(my_dict.values())
# print(my_dict.pop('one'))
# my_dict['one'] = my_dict['four']
# print(my_dict)


# my_set = {1, 2, 3, 4, 2, 5, 6, 7}
# print(my_set)
# my_f_set = frozenset((1, 2, 3, 4, 2, 5, 6, 7,))
# print(my_f_set)
# not_set = {1, 2, 3, 4, 2, 5, 6, 7, ['a', 'b']} # TypeError: unhashable type: 'list'


# my_set = {3, 4, 2, 5, 6, 1, 7}
# my_set.add(9)
# print(my_set)
# my_set.add(7)
# print(my_set)
# my_set.add(9, 10) # TypeError: set.add() takes exactly one argument (2 given)
# my_set.add((9, 10))
# print(my_set)


# my_set = {3, 4, 2, 5, 6, 1, 7}
# other_set = {1, 4, 42, 314}
# new_set = my_set.intersection(other_set)
# print(f'{my_set = }\n{other_set = }\n{new_set = }')


# my_set = {3, 4, 2, 5, 6, 1, 7}
# other_set = {1, 4, 42, 314}
# new_set = my_set.union(other_set)
# print(f'{my_set = }\n{other_set = }\n{new_set = }')
# new_set_2 = my_set | other_set
# print(f'{my_set = }\n{other_set = }\n{new_set_2 = }')


# my_set = {3, 4, 2, 5, 6, 1, 7}
# print(42 in my_set)






