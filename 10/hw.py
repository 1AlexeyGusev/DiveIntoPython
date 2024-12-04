# Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.

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

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, *args):
        if animal_type == "Fish":
            return Fish(*args)
        elif animal_type == "Bird":
            return Bird(*args)
        elif animal_type == "Mammal":
            return Mammal(*args)
        else:
            raise ValueError(f"Неизвестный тип животного: {animal_type}")

if __name__ == '__main__':
    try:
        fish = AnimalFactory.create_animal("Fish", "Немо", "Клоун", "соленая")
        bird = AnimalFactory.create_animal("Bird", "Попугай", 25, True)
        mammal = AnimalFactory.create_animal("Mammal", "Собака", "коричневый", True)

        print(fish.info())
        print(bird.info())
        print(mammal.info())
    except ValueError as e:
        print(e)