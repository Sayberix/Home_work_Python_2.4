# 1. Вычислить число c заданной точностью d

#Пример:

#- при d = 0.001, π = 3.141   
#    Ввод: 0.01
#    Вывод: 3.14

#    Ввод: 0.001
#    Вывод: 3.141

import math as m

def toFixed(number: float, digits: int) -> str:
    return f"{number:.{digits}f}"

accuracy = input('Введите точность через знак разделитель "." (например - "0.001"):')
discharge = len(str(accuracy).split('.')[1])
pi = 2 * (m.asin(m.sqrt(1 - 1 ** 2)) + m.fabs(m.asin(1)))
print('число PI с заданной точностью:',toFixed(pi,discharge))