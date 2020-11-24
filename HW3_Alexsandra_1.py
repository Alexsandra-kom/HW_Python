# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def div(x, y):
    try:
        z = x / y
        return round(z, 2)
    except ZeroDivisionError:
        return "Делитель y не должен быть равен нулю"
    except ValueError:
        return "Введите только числа"


print(div(int(input("Введите делимое х = ")), int(input("Введите делитель y = "))))