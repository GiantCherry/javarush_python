# Перегрузка операторов индексации

# Напишите класс Matrix, который будет представлять двумерную матрицу и поддерживать перегрузку операторов индексации ([]).
# Реализуйте методы __getitem__ и __setitem__.

class Matrix:
    # Напишите тут ваш код
    def __init__(self, rows, cols, fill_value=0):
        self.rows = rows
        self.cols = cols
        self.data = [[fill_value for _ in range(cols)] for _ in range(rows)]

    def __getitem__(self, indices):
        row, col = indices
        if row >= self.rows or col >= self.cols:
            raise IndexError("Index out of range")
        return self.data[row][col]

    def __setitem__(self, indices, value):
        row, col = indices
        if row >= self.rows or col >= self.cols:
            raise IndexError("Index out of range")
        self.data[row][col] = value

# Пример использования
matrix = Matrix(3, 3)
matrix[0, 0] = 1
print(matrix[0, 0])  # Вывод: 1