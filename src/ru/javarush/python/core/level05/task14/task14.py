# Фильтрация
import random
# Напишите программу, которая создает список из 20 случайных чисел в диапазоне от 1 до 100 с использованием List Comprehension.
# Затем с использованием List Comprehension создает новый список, содержащий только четные числа из исходного списка.
# Программа должна вывести оба списка.

# Напишите тут ваш код
randoms = [random.randint(1, 100) for i in range(20)]
randoms_even = [i for i in randoms if i % 2 == 0]

print(randoms)
print(randoms_even)