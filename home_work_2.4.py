# 4. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.

# Пример:

# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.

import random as r

def polynomial_formation(k_func: int) -> str:
    degree_list = ['', '', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']
    my_list_coef = rand_coef(k_func)
    list_polynomial = ''
    for i in range(k_func,0,-1):
        list_polynomial += str(my_list_coef[i - 2]) + '*x' + degree_list[i] + ' + '
        if i == 1:
            list_polynomial += str(my_list_coef[i]) + ' = 0'
    return list_polynomial

def rand_coef(k_func_2: int) -> list:
    my_list = []
    for i in range(k_func_2):
        my_list.append(r.randint(1,101))
    return my_list


k = int(input('Введите степень многочлена: '))

print('Сформированный многочлен: ',polynomial_formation(k))

