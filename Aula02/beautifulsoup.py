from bs4 import BeautifulSoup
import requests

html = requests.get("https://example.com").text
soup = BeautifulSoup(html, 'html.parser')
titulo = soup.find('h1').text
print(f"Título da página: {titulo}")