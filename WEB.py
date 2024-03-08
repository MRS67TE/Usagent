import requests

url = "https://web.telegram.org"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.95 Safari/537.36'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print(f"Сайт {url} успешно открыт с указанным User-Agent.")
else:
    print(f"Ошибка: {response.status_code}")