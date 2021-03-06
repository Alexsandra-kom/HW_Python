# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите,
# с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
# или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке). Далее запросите численность сотрудников
# фирмы и определите прибыль фирмы в расчете на одного сотрудника.

revenue = int(input("Введите значение выручки за период >>> "))
cost = int(input("Введите значение себестоимость за период >>> "))

profit = revenue - cost
if profit > 0:
    print(f'Прибыль компании составила - {profit}')
    profitability = round(profit / revenue, 2)
    print(f'Рентабиьность выручки составила - {profitability}')
    staff_number = int(input("Введите численность персонала >>> "))
    profit_for_staff = round(profit / staff_number, 2)
    print(f'Прибыль фирмы в расчете на одного сотрудника составляет - {profit_for_staff}')
elif profit == 0:
    print(f'Ваш финасовый результат равен нулю.')
else:
    print(f'Убыток компании составил - {abs(profit)}')
