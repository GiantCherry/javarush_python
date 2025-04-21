# Множественность

# Создайте пустое множество.
# Запросите у пользователя последовательно 5 чисел
# Для каждого из них создавайте отдельное множество и добавляйте его в первоначальное.
# Выведите полученный результат на экран.

# Напишите тут ваш код
set_0 = set()
for _ in range(5):
    number = int(input("Введите число: "))
    number_set = {number}
    set_0.update(number_set)

print(set_0)
'''
inputs = [int(input("Введите число: ")) for _ in range(5)]

set_1, set_2, set_3, set_4, set_5 = {inputs[0]}, {inputs[1]}, {inputs[2]}, {inputs[3]}, {inputs[4]}

print(set_1)
'''