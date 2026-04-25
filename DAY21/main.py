import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

headers = {
    'User-Agent': 'Mozilla/5.0 | (Windows 10 AT win x64)',
    'Accept': 'text/html',
    "Accept-Language": "ru-RU,ru;q=0.9"
}

data = {
    'name': 'german',
    'password': 'G1e9r2dwf'

}

url = os.getenv('URL')
session = requests.Session()

response = session.post(url, headers=headers)
text = response.text

print(response.status_code)
soup = BeautifulSoup(text, "html.parser")

for s in soup.find_all('strong'):
    text = s.get_text(strip=True)
    if text:
        print(text)