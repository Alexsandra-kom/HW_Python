# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка. В
# его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны
# быть реализованы методы перегрузки арифметических операторов: сложение (add()), вычитание (sub()), умножение (mul(
# )), деление (truediv()). Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и целочисленное (с округлением до целого) деление клеток, соответственно.

class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'Результат  {self.quantity * "*"}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        '''
        Выдает ошибку о том, что результат не число  при вычислении
        if int(Cell(self.quantity - other.quantity)) > 0:
            return Cell(int(self.quantity - other.quantity))
        else:
            return f'Операция вычитания невозможна'""
        '''
        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('Отрицательно!')

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row


cells1 = Cell(27)
cells2 = Cell(3)
print(cells1)
print(cells1 + cells2)
print(cells2 - cells1)
print(cells2.make_order(4))
print(cells1.make_order(2))
print(cells1 / cells2)
