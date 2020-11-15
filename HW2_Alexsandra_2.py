# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и
# 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка
# элементов необходимо использовать функцию input().


master_list = [int(user_list) for user_list in input("Введите элементы списка через пробел ").split()]

for user_list in range(1, len(master_list), 2):
    master_list[user_list - 1], master_list[user_list] = master_list[user_list], master_list[user_list - 1]

print(' '.join([str(user_list) for user_list in master_list]))
