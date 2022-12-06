# 3. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.
# 
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]

def find_repeating_elements(number: int, list_unique_elements: list) -> bool:
    for i in range(len(list_unique_elements)):
        if number == list_unique_elements[i] and i > 0:
            list_resault.pop(list_unique_elements[i])
            return False, list_unique_elements
    return True

list_number = [1, 1, 2, 3, 4, 4, 4, 2, 3]
list_resault = []
for i in range(1, len(list_number) - 1):
    if list_number[i] != list_number[i - 1] and list_number[i] != list_number[i + 1] and find_repeating_elements(list_number[i],list_resault):
        list_resault.append(list_number[i])
print('Список неповторяющихся элементов:',list_resault)