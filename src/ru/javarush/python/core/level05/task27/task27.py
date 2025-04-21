# Сумма кортежей
import random
# Напишите программу, которая создает кортеж, содержащий несколько вложенных кортежей из целых чисел.
# Программа должна использовать цикл for для вычисления суммы всех элементов во вложенных кортежах и вывести результат.

# Напишите тут ваш код
inputs = (tuple(random.randint(1, 100) for _ in range(random.randint(5, 10))),
          tuple(random.randint(1, 100) for _ in range(random.randint(5, 10))),
          tuple(random.randint(1, 100) for _ in range(random.randint(5, 10))),
          )
summa = 0
for inner_inputs in inputs:
    for number in inner_inputs:
        summa += number
print(summa)

