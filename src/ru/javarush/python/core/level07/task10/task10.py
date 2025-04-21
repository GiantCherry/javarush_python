# Редактор.
from ru.javarush.python.core.level07.task09.task09 import updates

# Напишите программу, которая создает словарь с информацией о книге (название, автор, год издания).
# Программа должна:
# Изменить значение ключа "год издания".
# Использовать метод setdefault() для добавления нового ключа "издательство", если он отсутствует.
# Обновить значения нескольких элементов с использованием метода update().
# Вывести обновленный словарь после каждого изменения.

# Напишите тут ваш код
book = {'title': 'Title book', 'year': 2025, 'author': 'Author'}
book['year'] = 2024
print(book)

if 'publisher' not in book:
    book.setdefault('publisher', 'AST')
print(book)

updates = {'weight': 500, 'color': 'Color'}
book.update(updates)
print(book)