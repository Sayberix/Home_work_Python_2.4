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

#coef_pars = []
#for i in range(len(polynomial_1_str)):
#    if polynomial_1_str[i][0].isdigit() and int(polynomial_1_str[i][0]) != 0:
#        coef_pars.append(int(polynomial_1_str[i][0]))
#return coef_pars

polynomial_str_1 = recive_text_file('polynomial_1')
polynomial_str_2 = recive_text_file('polynomial_2')
...

#for i in range(len(list_number)):
#    list_number[i] = int(list_number[i])

#with open(file_path,'a') as minmax:
#    minmax.write(f'\n{min(list_number)} {max(list_number)}')

