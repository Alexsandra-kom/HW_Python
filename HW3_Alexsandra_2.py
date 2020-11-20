# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать
# вывод данных о пользователе одной строкой.


def my_func(name, surname, birth_year, city, email, phone):
    print(name, surname, birth_year, city, email, phone)


my_func(name='Sandra', surname='Kom', birth_year=1988, city='SPB', email='akom@mail.ru', phone='+7 905 333-33-33')
