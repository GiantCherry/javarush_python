# Использование traceback

# Напишите функцию divide_numbers, которая принимает два аргумента и делит первое число на второе.
# Если возникает исключение ZeroDivisionError, перехватите его и выведите стек-трейс, используя модуль traceback.

# Напишите тут ваш код
import traceback

def divide_numbers(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        traceback.print_exc()


