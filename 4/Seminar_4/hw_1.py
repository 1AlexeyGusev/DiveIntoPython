# Напишите функцию для транспонирования матрицы

def transponce_matrix(matrix):
    transponced = []
    for i in range(len(matrix[0])):
        new_row = []
        for row in matrix:
            new_row.append(row[i])
            transponced.append(new_row)
    return transponced


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(transponce_matrix(matrix))
