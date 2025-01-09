# Доработаем прямоугольник и добавим экономию памяти
# для хранения свойств экземпляра без словаря __dict__.

class Rectangle:
    __slots__ = ('_width', '_length')

    def __init__(self, width, length=None):
        self.width = width
        if length is not None:
            self.length = length
        else:
            self.length = width

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise ValueError('Ширина должна быть больше 0')

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if value > 0:
            self._length = value
        else:
            raise ValueError('Длина должна быть больше 0')

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
    rectangle = Rectangle(4, 6)
    print(rectangle)
