# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.

class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        return f'Имя животного: {self.name}'

class Fish(Animal):
    def __init__(self, name, species, water_type):
        super().__init__(name)
        self.species = species
        self.water_type = water_type

    def info(self):
        return f'{super().info()}, Вид: {self.species}, Тип воды: {self.water_type}'

class Bird(Animal):
    def __init__(self, name, wing_span, can_fly):
        super().__init__(name)
        self.wing_span = wing_span
        self.can_fly = can_fly

    def info(self):
        flying_ability = 'может летать' if self.can_fly else 'не может летать'
        return f'{super().info()}, Размах крыльев: {self.wing_span} см, {flying_ability}'

class Mammal(Animal):
    def __init__(self, name, fur_color, is_domestic):
        super().__init__(name)
        self.fur_color = fur_color
        self.is_domestic = is_domestic

    def info(self):
        domestic_status = 'домашнее' if self.is_domestic else 'дикое'
        return f'{super().info()}, Цвет шерсти: {self.fur_color}, Статус: {domestic_status}'

if __name__ == '__main__':
    bird = Bird('Гошан', 14, True)
    print(bird.info())
