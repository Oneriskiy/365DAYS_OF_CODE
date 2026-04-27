import requests
from bs4 import BeautifulSoup

session = requests.Session()
url = ''

response = session.get(url)
soup = BeautifulSoup(response.text)


for i in soup.find_all('a', class_='g-link'):
    print(i.get_text(strip=True))