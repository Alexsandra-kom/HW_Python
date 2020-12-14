# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.

class DivisionNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator


def divide_null(divider, denominator):
    try:
        return round(divider / denominator, 2)
    except:
        return (f"Деление на ноль недопустимо")


print(divide_null(int(input("Введите делимое >>> ")), int(input("Введите делитель >>> "))))
