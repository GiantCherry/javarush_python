# Словарь из списка кортежей.

# Напишите программу, которая создает список кортежей с информацией о сотрудниках (например, имя и должность).
# Программа должна:
# Использовать dictionary comprehension для создания словаря из списка кортежей.
# Вывести созданный словарь.

# Напишите тут ваш код
employes = [
    ('Vasay', 'engeneer_0'),
    ('Vova', 'engeneer_1'),
    ('Petya', 'engeneer_2'),
    ('Misha', 'engeneer_3'),
]

employees_tuple = {key: value for (key, value) in employes}

print(employees_tuple)
