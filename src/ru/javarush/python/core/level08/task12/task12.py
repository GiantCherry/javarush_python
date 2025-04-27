# Длительность работы.

# Напишите программу, которая создает декоратор для измерения времени выполнения функции.
# Программа должна:
# Определить декоратор time_decorator, который измеряет и выводит время выполнения функции.
# Применить декоратор к функции compute_square(n), которая вычисляет квадрат числа и имитирует задержку с помощью time.sleep().
# Вызвать функцию compute_square(n).

# Напишите тут ваш код
import time

def time_decorator(func):
    def wrapper(n):
        start_time = time.time()
        result = func(n)
        end_time = time.time()
        print(f"Время выполнения: {end_time - start_time} секунд")
        return result
    return wrapper

@time_decorator
def compute_square(n):
    time.sleep(2)  # имитация задержки
    return n * n

compute_square(5)