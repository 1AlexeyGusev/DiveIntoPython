# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

def replace_s() -> None:
    global datas, s, names, sx
    dict_values = {}

    for var_name, var_value in globals().items():
        if var_name.endswith('s') and var_name != 's':
            new_var_name = var_name[:-1]
            dict_values[new_var_name] = var_value
            globals()[var_name] = None

    for new_var_name, value in dict_values.items():
        globals()[new_var_name] = value


datas = [42, -73, 12, 85, -15, 2]
s = 'Hello world!'
names = ('NoName', 'OtherName', 'NewName')
sx = 42

replace_s()
print(datas, s, names, sx, sep='\n')
