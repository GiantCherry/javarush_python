# Проверка существования файла

# Напишите программу, которая проверяет, существует ли файл example.txt, и если существует, удаляет его.

# Напишите тут ваш код
import os

if os.path.isfile('example.txt'):
    os.remove('example.txt')
    print('File removed')
