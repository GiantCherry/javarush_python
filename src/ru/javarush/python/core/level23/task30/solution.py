from bs4 import BeautifulSoup

# Путь к HTML-файлу, который будем анализировать
file_path = "example.html"  # Укажите путь к вашему HTML-файлу

# Открываем HTML-файл и читаем его содержимое
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Создание объекта BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Извлечение элементов списка <li>
li_elements = soup.find_all('li')

# Формирование списка Python из текста элементов
items = [item.getText() for item in li_elements]

# Вывод результата
print(items)