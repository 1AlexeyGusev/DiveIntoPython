# Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину и ширину
# на дескриптор с валидацией размера.


class Range:
    def __set_name__(self, owner, name):
        self.param_name = ' ' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if value < 1:
            raise ValueError

class Rectangle:

    width = Range()
    length = Range()

    def __init__(self, width, length=None):
        self.width = width
        if length is not None:
            self.length = length
        else:
            self.length = width

    def perimeter(self):
        return (self.length + self.width) * 2

    def area(self):
        return self.width * self.length

    def __add__(self, other):
        if isinstance(other, Rectangle):
            new_perimeter = self.perimeter() + other.perimeter()
            # Создаем новый экземпляр с равными сторонами для простоты
            new_side = new_perimeter / 4
            return Rectangle(new_side)

    def __sub__(self, other):
        if isinstance(other, Rectangle):
            new_perimeter = self.perimeter() - other.perimeter()
            if new_perimeter < 0:
                raise ValueError("Результат вычитания не может быть отрицательным.")
            # Создаем новый экземпляр с равными сторонами для простоты
            new_side = new_perimeter / 4
            return Rectangle(new_side)

    def __eq__(self, other):
        return isinstance(other, Rectangle) and self.area() == other.area()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return isinstance(other, Rectangle) and self.area() < other.area()

    def __le__(self, other):
        return isinstance(other, Rectangle) and self.area() <= other.area()

    def __gt__(self, other):
        return isinstance(other, Rectangle) and self.area() > other.area()

    def __ge__(self, other):
        return isinstance(other, Rectangle) and self.area() >= other.area()

    def __str__(self):
        return f'Длина прямоугольника = {self.length} \nШирина прямоугольника = {self.width}'


if __name__ == '__main__':
    rectangle = Rectangle(1, 6)
    print(rectangle)
