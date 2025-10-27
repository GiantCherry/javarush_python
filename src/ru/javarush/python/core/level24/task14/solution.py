import random
import requests

# Список прокси-серверов. Для примера указаны фиктивные адреса, замените их на реальные.
proxy_list = [
    'http://123.456.789.1:8080',
    'http://987.654.321.0:8080',
    'http://192.168.1.1:8080'
]

# Случайный выбор прокси-сервера из списка
selected_proxy = random.choice(proxy_list)

# Настройка прокси для библиотеки requests
proxies = {
    'http': selected_proxy,
    'https': selected_proxy
}

# Отправка GET-запроса через выбранный прокси-сервер
response = requests.get( "http://example.com", proxies=proxies)

# Вывод содержимого страницы в консоль
print(response.text)