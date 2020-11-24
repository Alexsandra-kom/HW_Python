# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не
# должен быть бесконечным. Необходимо предусмотреть условие его завершения.
#
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором
# также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count
from itertools import cycle


def my_count_func(first_number, last_number):
    for el in count(first_number):
        if el > last_number:
            break
        else:
            print(el)


def my_cycle_func(my_list, iteration):
    i = 0
    iter = cycle(my_list)
    while i < iteration:
        print(next(iter))
        i += 1


my_count_func(first_number=int(input("Введите первое число: ")), last_number=int(input("Введите последнее число: ")))
my_cycle_func(my_list=["red", 6, "blue", 35, "white", 2], iteration=int(input("Введите число повторений: ")))