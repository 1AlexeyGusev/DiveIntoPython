# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.


class Rectangle:
    def __init__(self, width, length=None):
        self.width = width
        self.length = length
        if length:
            self.length = length
        else:
            self.length = width

    def perimeter(self):
        return (self.length + self.width) * 2

    def area(self):
        return self.width*self.length

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


if __name__ == '__main__':
    rectangle = Rectangle(4, 6)
    print(f'Периметр прямоугольника = {rectangle.perimeter()}')
    print(f'Площадь прямоугольника = {rectangle.area()}')