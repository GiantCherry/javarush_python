# Обработка исключений.

# Напишите функцию safe_division, которая принимает два числа и выполняет их деление.
# Обработайте исключения, которые могут возникнуть при делении на ноль
# и при передаче некорректных значений (например, строки вместо чисел).
# Функция должна возвращать сообщение об ошибке или результат деления.

# Напишите тут ваш код
def save_division(x, y):
    try:
        result = x / y
    except TypeError:
        return  'Type Error'
    except ZeroDivisionError:
        return 'Zero Division'
    except:
        return 'Error!'
    else:
        return result

