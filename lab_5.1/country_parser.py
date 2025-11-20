import requests
from bs4 import BeautifulSoup
import csv
import sys
import time
import os

URL = "https://geo.koltyrin.ru/eng_countries_of_the_world.php"
CACHE_FILE = "cache_page.html"

def load_page():
    """Загружаем страницу либо из кэша, либо из интернета"""
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                return f.read()
        except Exception:
            pass

    try:
        resp = requests.get(URL, timeout=15)
        resp.raise_for_status()
        html = resp.text
        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            f.write(html)
        return html
    except requests.RequestException as e:
        print(f"Ошибка загрузки страницы: {e}")
        return None

def normalize(name: str) -> str:
    """Приводим название к нижнему регистру и убираем пробелы"""
    return name.lower().strip()

def parse_data(country_list):
    """Парсим таблицу и достаём данные по нужным странам"""
    html = load_page()
    if not html:
        return []

    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table")
    if not table:
        print("Таблица не найдена на странице")
        return []

    rows = table.find_all("tr")
    result = []
    norm_list = [normalize(c) for c in country_list]

    for row in rows[1:]:  # пропускаем заголовок
        cols = row.find_all("td")
        if len(cols) >= 4:
            country = cols[0].get_text(strip=True)
            capital = cols[1].get_text(strip=True)
            area = cols[2].get_text(strip=True).replace(",", "")
            population = cols[3].get_text(strip=True).replace(",", "")

            norm_country = normalize(country)
            for c in norm_list:
                if c == norm_country or c in norm_country or norm_country in c:
                    result.append([country, capital, area, population])
                    break
    return result

def main():
    if len(sys.argv) < 3:
        print("Использование: python country_parser.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file, "r", encoding="utf-8-sig") as f:
            countries = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"Ошибка чтения {input_file}: {e}")
        sys.exit(1)

    data = parse_data(countries)
    time.sleep(1)  # пауза между запросами

    try:
        with open(output_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["country", "city", "area", "population"])
            writer.writerows(data)
        print(f"Данные сохранены в {output_file}")
    except Exception as e:
        print(f"Ошибка записи CSV: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()