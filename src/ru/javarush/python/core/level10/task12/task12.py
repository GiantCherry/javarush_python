# Переупаковка исключения

# Напишите функцию validate_input, которая принимает строку и проверяет,
# что она не пустая и что ее длина не превышает 10 символов.
# Если строка пустая, запустите ValueError с сообщением "Input cannot be empty".
# Если строка слишком длинная, запустите ValueError с сообщением "Input is too long".
# Затем перехватите это исключение и переупакуйте его в пользовательское исключение InputValidationError, сохранив исходное исключение как причину.

# Напишите тут ваш код
class InputValidationError(Exception):
    def __init__(self, message, original_exception):
        super().__init__(message)
        self.original_exception = original_exception

def validate_input(s):
    try:
        length = len(s)
        if length == 0:
            raise ValueError("Input cannot be empty")
        if length > 10:
            raise ValueError("Input is too long")
    except ValueError as e:
        raise InputValidationError("Input validation error", e)

# Пример использования:
try:
    validate_input("")
except InputValidationError as e:
    print(f"Caught custom exception: {e}")
    print(f"Original exception: {e.original_exception}")