# 3. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.
# 
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]


def find_repeating_elements(list_number: list) -> dict:
    dict_elements = {}
    for i in range(len(list_number)):
        count = 1
        for k in range(len(list_number)):
            if list_number[i] == list_number[k] and i is not k:
                count += 1
        dict_elements[i] = count
    return dict_elements

def deleting_elements(my_list: list, my_dict: dict) -> list:
    #for i in range(len(my_list) - 1,0,-1):
    #    ...
    #    if my_dict[i] > 1:
    #        my_list.pop(i)
    i = len(my_list) - 1
    while i >=0:
        if my_dict[i] > 1:
            my_list.pop(i)
        i -= 1
    return my_list


list_number = [1, 1, 2, 3, 4, 4, 4]

print('Список неповторяющихся элементов:',deleting_elements(list_number, find_repeating_elements(list_number)))