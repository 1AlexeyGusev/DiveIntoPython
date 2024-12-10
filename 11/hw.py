# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц

class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0

    def __str__(self):
        # Метод для вывода матрицы в удобочитаемом виде
        return '\n'.join(['\t'.join(map(str, row)) for row in self.data])

    def __eq__(self, other):
        # Сравнение матриц
        return isinstance(other, Matrix) and self.data == other.data

    def __add__(self, other):
        # Сложение матриц
        if not isinstance(other, Matrix) or self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны быть одинакового размера для сложения.")

        result = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __mul__(self, other):
        # Умножение матриц
        if not isinstance(other, Matrix) or self.cols != other.rows:
            raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы.")

        result = [[0] * other.cols for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result[i][j] += self.data[i][k] * other.data[k][j]

        return Matrix(result)


# Пример использования
matrix1 = Matrix([[1, 2, 3], [4, 5, 6]])
matrix2 = Matrix([[7, 8, 9], [10, 11, 12]])

# Вывод матриц
print("Matrix 1:")
print(matrix1)
print("\nMatrix 2:")
print(matrix2)

# Сложение матриц
result_add = matrix1 + matrix2
print("\nСложение матриц:")
print(result_add)

# Умножение матриц
matrix3 = Matrix([[1, 2], [3, 4], [5, 6]])
result_mul = matrix1 * matrix3
print("\nУмножение матриц:")
print(result_mul)
