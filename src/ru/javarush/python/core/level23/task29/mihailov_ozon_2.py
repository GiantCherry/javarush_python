from requests_html import HTMLSession

def parse_ozon_requests_html():
    session = HTMLSession()

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    try:
        url = 'https://www.ozon.ru/seller/santegra-1037570/?miniapp=seller_1037570'
        response = session.get(url, headers=headers)

        # Запускаем JavaScript
        response.html.render(sleep=2, timeout=20)

        soup = BeautifulSoup(response.html.html, 'html.parser')
        print(soup.prettify()[:2000])

    except Exception as e:
        print(f"Ошибка: {e}")


parse_ozon_requests_html()