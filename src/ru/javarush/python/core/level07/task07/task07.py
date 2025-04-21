# Три проверки.

# Напишите программу, которая создает словарь с информацией о книге (например, название, автор, год издания).
# Программа должна:
# Проверить наличие ключа "author" с использованием оператора in.
# Проверить наличие ключа "publisher" с использованием метода get().
# Проверить наличие ключа "title" с использованием метода keys().

# Напишите тут ваш код
book = {'title': 'War and Peace', 'author': 'Tolstoy', 'publisher': 1869}

print('author' in book)
publisher = book.get('publisher')
if publisher is not None:
    print(f'ключ \'publisher\' присутствует в словаре')
else:
    print(f'ключ \'publisher\' не присутствует в словаре')

print('title' in book.keys())


