# Обратный кортеж

# Напишите программу, которая создает кортеж из произвольного количества элементов, запрашиваемых у пользователя.
# Затем программа должна вывести кортеж в обратном порядке с использованием среза.

# Напишите тут ваш код
inputs = (tuple(input("Введите данные: ").split(',')))

print(inputs[::-1])