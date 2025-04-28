# Работа с директориями.

# Напишите программу, которая создает директорию, переходит в нее, создает файл внутри этой директории,
# записывает в файл текст, а затем читает и выводит его содержимое.
# Программа должна:
# Создать директорию test_directory.
# Перейти в директорию test_directory.
# Создать файл test_file.txt и записать в него строку "Hello, World!".
# Прочитать содержимое файла test_file.txt и вывести его на экран.
# Удалить файл и директорию.

# Напишите тут ваш код
import os

os.makedirs('test_directory', exist_ok=True)
os.chdir('test_directory')

file_name = "test_file.txt"
with open(file_name, 'w') as file:
    file.write("Hello, World!")

with open(file_name, 'r') as file:
    content = file.read()
    print(content)

os.remove(file_name)

os.chdir('..')
os.rmdir('test_directory')