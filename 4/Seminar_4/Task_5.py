# Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.
import decimal


def func(names: list[str], salary: list[float], bonus: list[str]) -> dict[str: decimal.Decimal]:
    result = {}
    for name, salary, bonus in zip(names, salary, bonus):
        result[name] = salary * decimal.Decimal(bonus.replace('%', '')) / 100
    return {name: float(value) for name, value in result.items()}
    # print(f"{names} получил премию {float((salary/100)*bonus)}")


n = ['Иван', 'Николай', 'Петр', 'Харитон']
s = [125_000, 96_000, 109_000, 100_000]
a = ['10%', '25.5%', '13.3%', '42.73%']

print(func(n, s, a))
