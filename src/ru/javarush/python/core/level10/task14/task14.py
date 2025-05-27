# Иерархия пользовательских исключений

# Создайте базовый класс исключений ApplicationError и два подкласса NegativeValueError и ValueTooLargeError.
# Реализуйте функцию check_number, которая будет вызывать соответствующее исключение, если число отрицательное или слишком большое.
# Обработайте исключения в блоке try-except.

# Напишите тут ваш код
class ApplicationError(Exception):
    pass

class NegativeValueError(ApplicationError):
    def __init__(self, value, message="Значение не должно быть меньше нуля"):
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}: {self.value}'

class ValueTooLargeError(ApplicationError):
    def __init__(self, value, message="Значение не должно быть слишком велико"):
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}: {self.value}'


def check_number(number):
    if number < 0:
        raise NegativeValueError(number)
    elif number > 1000:
        raise ValueTooLargeError(number)

try:
    check_number(2000)
except NegativeValueError as e:
    print(f'Произошло исключение: {e}')
except ValueTooLargeError as e:
    print(f'Произошло исключение: {e}')
except ApplicationError as e:
    print(f'Общее исключение приложения: {e}')

