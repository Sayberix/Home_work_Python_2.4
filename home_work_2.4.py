# 5. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов (складываются числа, у которых "х" в одинаковых степенях). 
# Пример того, что будет в итоговом файле: 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0

# 'r' - чтение
# 'w' - перезапись (если файла нет, он создается)
# 'a' - дозапись
# 'r+' - чтение + запись

from pathlib import Path

# запись в файл:
#file_path = Path('data', 'task_1.txt')
#with open(file_path,'w') as data:
#    data.write('1 8 6 5 0 7 3 5 2 6 5 3 0 1')

#def first_digit(word: str) -> int:
#    for i in range(len(word)):
#        return 

def recive_text_file (name_file: str) -> str:
    file_path = Path(name_file, name_file + '.txt')
    with open(file_path,'r') as polynomial:
        polynomial_str = polynomial.read().split()
    return polynomial_str

def recive_coef (polynomial_str: str) -> list:
    list_coef = []
    for i in range(len(polynomial_str)):
        if polynomial_str[i][0].isdigit() and int(polynomial_str[i][0]) != 0:
            list_coef.append(int(polynomial_str[i][0]))
    return list_coef

def sum_coef(list_coef_1: list, list_coef_2: list) -> list:
    sum_coef_list = []
    #try:
    if len(list_coef_1) == len(list_coef_2):
         for i in range(len(list_coef_1)):
             sum_coef_list.append(list_coef_1[i] + list_coef_2[i])
        #else:
        #    raise Exception("Многочлены не одинаковой степени! Программа завершает работу!")
    return sum_coef_list

def polynomial_formation(sum_coef_list: list) -> str:
    degree_list = ['', '', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']
    list_polynomial = ''
    for i in range(len(sum_coef_list) - 1,-1,-1):
        if i != 0:
            list_polynomial += str(sum_coef_list[len(sum_coef_list) - 1 - i]) + '*x' + degree_list[i] + ' + '
        else:
            list_polynomial += str(sum_coef_list[len(sum_coef_list) - 1 - i]) + ' = 0'
    return list_polynomial


# Получаем сырые списки строк многочленов
polynomial_str_1 = recive_text_file('polynomial_1')
polynomial_str_2 = recive_text_file('polynomial_2')

# Получаем списки кооэфициентов многочленов
list_coef_1 = recive_coef(polynomial_str_1)
list_coef_2 = recive_coef(polynomial_str_2)

# Перемножаем кооэфициенты многочленов и выводим
print(polynomial_formation(sum_coef(list_coef_1, list_coef_2)))




#for i in range(len(list_number)):
#    list_number[i] = int(list_number[i])

#with open(file_path,'a') as minmax:
#    minmax.write(f'\n{min(list_number)} {max(list_number)}')

