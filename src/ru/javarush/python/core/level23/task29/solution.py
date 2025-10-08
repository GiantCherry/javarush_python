from bs4 import BeautifulSoup

# Путь к HTML-файлу, который будем анализировать
file_path = "example.html"  # Укажите путь к вашему HTML-файлу

# Открываем HTML-файл и читаем его содержимое
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Создание объекта BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Извлечение заголовков таблицы
table = soup.find('table')
headears = []
header_row = table.find('tr')
for header in header_row:
    if header.text.strip():
        headears.append(header.text.strip())

# Вывод заголовков на экран
print(headears)