import requests
from bs4 import BeautifulSoup

# URL для загрузки
url = 'https://example.com'

# Выполнение HTTP-запроса для получения HTML-кода страницы
response = requests.get(url)

# Парсинг HTML-кода с помощью BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Извлечение заголовка страницы
title = soup.title.text

# Вывод заголовка страницы
print('Title: ', title)