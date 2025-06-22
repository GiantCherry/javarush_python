# Обработка ошибок при работе с файлами

# Напишите программу, которая открывает файл example.txt в режиме добавления, записывает в него строку "Новая линия.".
# Нужно корректно обрабатывать исключение FileNotFoundError, закрывая файл в любом случае.

# Напишите тут ваш код
file = None

try:
    file = open('example.txt', 'a')
    file.write('\nНовая линия.')
except:
    print('Something went wrong!')
finally:
    if file:
        file.close()

