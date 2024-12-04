# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании экземпляра.
# У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.


class Rectangle():
    def __init__(self, width, length=None):
        self.width = width
        self.length = length
        if length:
            self.length = length
        else:
            self.length = width

    def perimetr(self):
        return (self.length + self.width) * 2

    def area(self):
        return self.width*self.length

if __name__ == '__main__':
    rectangle = Rectangle(4, 6)
    print(f'Периметр прямоугольника = {rectangle.perimetr()}')
    print(f'Площадь прямоугольника = {rectangle.area()}')
