# Извлечение информации из исключения

# Напишите функцию read_integer, которая принимает строку и пытается преобразовать её в целое число.
# Если возникает ValueError, обработайте исключение и выведите аргументы ошибки и тип ошибки.
# Дополнительно, сохраните исключение в переменной и выведите её за пределами блока except.

# Напишите тут ваш код
def read_integer(x):
    exception = None
    try:
        return int(x)
    except ValueError as e:
        exception = e
        print(f"Произошла ошибка: {e}")
        print(f"Тип ошибки: {type(e)}")
        print(f"Аргументы ошибки: {e.args}")

    print(f"Произошла ошибка: {exception}")
    print(f"Тип ошибки: {type(exception)}")
    print(f"Аргументы ошибки: {exception.args}")
