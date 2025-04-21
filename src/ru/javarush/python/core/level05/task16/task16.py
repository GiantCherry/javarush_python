# Сортировка строк по длине

# Напишите программу, которая создает список из 5 строк, запрашиваемых у пользователя.
# Затем программа должна отсортировать список по длине строк и вывести отсортированный список.

# Напишите тут ваш код
'''
def get_len(string):
    return len(string)

lists = []
for _ in range(5):
    lists.append(input("Введите значение: "))

lists_sorted = sorted(lists, key=get_len)

print(lists_sorted)
'''

lists = []
for _ in range(5):
    lists.append(input("Введите значение: "))

lists_sorted = sorted(lists, key=len)

print(lists_sorted)
