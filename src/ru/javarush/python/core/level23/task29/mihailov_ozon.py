from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time


def parse_ozon_selenium():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')

    driver = webdriver.Chrome(options=chrome_options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    try:
        url = 'https://www.ozon.ru/seller/santegra-1037570/?miniapp=seller_1037570'
        driver.get(url)

        # Ждем загрузки контента
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        time.sleep(3)  # Дополнительная задержка

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Парсим информацию о продавце
        seller_name = soup.find('h1')
        if seller_name:
            print(f"Название продавца: {seller_name.text.strip()}")

        # Ищем рейтинг
        rating = soup.find('span', string=lambda text: text and '₽' in text)
        if rating:
            print(f"Рейтинг: {rating.text.strip()}")

        # Сохраняем HTML для анализа
        with open('ozon_page.html', 'w', encoding='utf-8') as f:
            f.write(soup.prettify())

        print("Страница сохранена в ozon_page.html")

    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        driver.quit()


parse_ozon_selenium()