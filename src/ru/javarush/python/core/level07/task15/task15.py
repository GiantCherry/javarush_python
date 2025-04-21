# Заморозка

# Напишите программу, которая создает несколько объектов типа frozenset из различных итерируемых объектов (список, строка).
# Программа должна:
# Создать frozenset из списка.
# Создать frozenset из строки.
# Выполнить объединение, пересечение, разность и симметрическую разность двух frozenset множеств.
# Вывести результаты каждой операции.

# Напишите тут ваш код
fset_1 = frozenset([1, 2, 3])
fset_2 = frozenset('abc')

print(fset_1.union(fset_2))
print(fset_1.intersection(fset_2))
print(fset_1.difference(fset_2))
print(fset_1.symmetric_difference(fset_2))

