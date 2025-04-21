# Случайный аргумент
import random
# Напишите функцию  print_random(a,b,c), которая выводит на экран случайно выбранный переданный аргумент.

# Напишите тут ваш код
def print_random(a, b, c):
    randoms = [a, b, c]
    rand = random.choice(randoms)
    print(f"{rand}")


print_random(1, 2, 3)