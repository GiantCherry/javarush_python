# Проверка на пустоту.

# Напишите программу, которая создает несколько словарей с различным количеством элементов.
# Программа должна:
# Вывести количество элементов в каждом словаре.
# Проверить, пустой ли каждый словарь, и вывести соответствующее сообщение.
# Для проверки пустоты словаря нужно создать функцию check_empty

# Напишите тут ваш код
def check_empty(dict):
    return False if len(dict) > 0 else True

# dict_1 = {'1': 1, '2': 2, '3': 3}
dict_1 = {}
dict_2 = {'4': 4, '5': 5, '6': 6, '7': 7}

print(len(dict_1))
print(len(dict_2))

if check_empty(dict_1):
    print(f'Словарь {dict_1} - пустой')
else:
    print(f'Словарь {dict_1} - не пустой')

if check_empty(dict_2):
    print(f'Словарь {dict_2} - пустой')
else:
    print(f'Словарь {dict_2} - не пустой')



