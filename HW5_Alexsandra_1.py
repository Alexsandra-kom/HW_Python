# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

user_list = []
while True:
    line = input("Введите текст: ")
    if line == '':
        print(user_list)
        exit()
    else:
        newline = line + '\n'
        user_list.append(newline)

    with open("test.txt", "w") as file_obj:
        file_obj.writelines(user_list)

