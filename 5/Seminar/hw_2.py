# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии

names = ['Alex', 'Bob', 'John', 'Ivan']
rates = [10_000, 11_000, 9_000, 15_000]
premiums = ['10.00%', '12.00%', '20.50%', '18.05%']

result = {name: rate * (float(premium[:-1]) / 100) for name, rate, premium in zip(names, rates, premiums)}

print(result)

