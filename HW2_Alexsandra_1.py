# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных
# каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.

exp_int = 10
exp_float = 5.5
exp_str = "Печенька"
exp_bool = True
exp_list = ['56', '2', '34']
exp_tuple = ('a', '4', 'c')
exp_dict = {'name': 'Карл', 'age': '15'}

master_list = [exp_int, exp_float, exp_str, exp_bool, exp_list, exp_tuple, exp_dict]

for i in master_list:
    print(f'{i} относится к типу данных -  {type(i)}')
