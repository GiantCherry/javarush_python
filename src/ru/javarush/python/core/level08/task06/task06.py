# Замыкание.

# Напишите программу, которая создает функцию фильтра с использованием замыканий.
# Программа должна:
# Определить внешнюю функцию make_filter(threshold), которая создает и возвращает внутреннюю функцию filter_func(value).
# Внутренняя функция filter_func(value) должна возвращать True, если value больше threshold.
# Создать несколько функций фильтров с различными пороговыми значениями и
# использовать их для фильтрации списка данных, выводя результат на экран.

# Напишите тут ваш код
def make_filter(threshold):
    def filter_func(value):
        return value > threshold

    return filter_func

values = [1, 4, 99, 15, 37, 11, 64, 32, 9, 19]

filter_above_10 = make_filter(10)
list_10 = list(filter(filter_above_10, values))
print(list_10)

filter_above_50 = make_filter(50)
list_50 = list(filter(filter_above_50, values))
print(list_50)