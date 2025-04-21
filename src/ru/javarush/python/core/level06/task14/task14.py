# Разность множеств
import random
# Напишите программу, которая создает два множества из случайных чисел.
# Первое множество содержит 10 случайных чисел в диапазоне от 1 до 20, а второе множество содержит 10 случайных чисел в диапазоне от 10 до 30.
# Программа должна найти разность первого множества со вторым с использованием метода difference().
# И симметрическую разность с использованием метода symmetric_difference().
# Программа должна вывести оба результата.

# Напишите тут ваш код
set_1 = {random.randint(1, 20) for _ in range(10)}
set_2 = {random.randint(10, 30) for _ in range(10)}

difference_set = set_1.difference(set_2)
symmetric_difference_set = set_1.symmetric_difference(set_2)

print(difference_set)
print(symmetric_difference_set)