# Копирование файла

# Напишите программу, которая копирует файл source.txt в файл destination.txt

# Напишите тут ваш код

with open('source.txt', 'r') as file:
    source = file.read()

with open('destination.txt', 'w') as file:
    destination = file.write(source)

