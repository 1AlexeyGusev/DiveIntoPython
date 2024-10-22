# ✔ Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами. Код должен расширяться
# на любое большее количество друзей.

hike = {
    'Aaz': ('спички', 'спальник', 'дрова'),
    'Skeeve': ('спальник', 'спички', 'вода', 'еда'),
    'Tananda': ('вода', 'спички', 'косметичка'),
}

all_things = set()
# all_things.update(*hike.values())
# print(all_things)
for values in hike.values():
    all_things.update(values)
print(f'Полный список вещей: {all_things = }')

unique ={}
for master_friend, master_thing in hike.items():
    for slave_friend, slave_thing in hike.items():
        if master_friend != slave_friend:
            if master_friend not in unique:
                unique[master_friend] = set(master_thing) - set(slave_thing)
            else:
                unique[master_friend] -= set(slave_thing)
print(f'Уникальный список вещей: {unique}')

dublicates = set(all_things)
uniq_things = set()
uniq_things.update(*unique.values())
print(uniq_things)
dublicates -= uniq_things
print(dublicates)
