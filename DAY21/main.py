import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv('URL')
response = requests.get(url)
text = response.text

soup = BeautifulSoup(text, "html.parser")

for h in soup.find_all(["h1", "h2", "h3"]):
    text = h.get_text(strip=True)
    if text:
        print(text)