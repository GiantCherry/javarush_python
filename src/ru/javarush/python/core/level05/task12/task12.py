# Четкий список

# Напишите программу, которая создает список из 10 целых чисел.
# С использованием цикла for замените все четные элементы списка на строку "четное".
# Программа должна вывести обновленный список.

# Напишите тут ваш код
numbers = [i for i in range(10)]
for i, number in enumerate(numbers):
    if number % 2 == 0:
        numbers[i] = 'четное'

print(numbers)
