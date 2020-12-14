# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен
# принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.


class Matrix:
    def __init__(self, list_1, list_2) -> object:

        self.list_1 = list_1
        self.list_2 = list_2

    @property
    def __add__(self):
        matrix1 = [[0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                matrix1[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix1]))


my_matrix = Matrix([[6, 23, 34],
                    [5, 11, 23],
                    [22, 31, 9]],
                   [[54, 8, 2],
                    [6, 7, 39],
                    [7, 5, 42]])

print(my_matrix.__add__)
