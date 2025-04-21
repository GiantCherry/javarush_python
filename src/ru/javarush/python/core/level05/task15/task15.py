# Сортировки
import random
# Напишите программу, которая создает список из 10 случайных чисел в диапазоне от 1 до 100.
# Затем сортирует его по возрастанию и убыванию.
# Программа должна вывести исходный список, отсортированный по возрастанию и по убыванию списки.

# Напишите тут ваш код
randoms = [random.randint(1, 100) for _ in range(10)]
randoms_sorted = sorted(randoms)
randoms_sorted_reverse = sorted(randoms, reverse=True)

print(randoms)
print(randoms_sorted)
print(randoms_sorted_reverse)