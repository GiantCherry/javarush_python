# Чистим список
import random
# Напишите программу, которая создает список из 10 случайных чисел в диапазоне от 1 до 20.
# Затем программа должна удалить из списка все четные числа с использованием цикла.
# Программа должна вывести исходный и обновленный списки.

# Напишите тут ваш код
randoms = [random.randint(1, 20) for _ in range(10)]
# even_randoms = [x for x in randoms if x % 2 != 0]
even_randoms = []

for random in randoms:
    if random % 2 != 0:
        even_randoms.append(random)

print(randoms)
print(even_randoms)
