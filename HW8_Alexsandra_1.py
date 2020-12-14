# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.

class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


def valid(day, month, year):
    if 1 <= day <= 31:
        if 1 <= month <= 12:
            if 2020 >= year >= 0:
                return f'Все нормально'
            else:
                return f'Некорректный год'
        else:
            return f'Некорректный месяц'
    else:
        return f'Некорректный день'


today = Data('14 - 12 - 2020')
print(today)
print(valid(14, 12, 2025))
print(valid(14, 13, 2020))
print(Data.extract('14 - 12 - 2010'))
print(today.extract('14 - 12 - 2020'))
print(valid(14, 12, 2020))
