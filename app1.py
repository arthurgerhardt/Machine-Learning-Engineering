import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://youtu.be/0_hecMDuaFQ"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

if response.status_code == 200:
    html_content = response.text # pegamos o conteúdo HTML da página
    print("Conteúdo HTML obtido com sucesso!")
else:
    print(f"Erro ao acessar a página: {response.status_code}")

for i in range(1, 7): # h1 a h6
    headers = soup.find_all(f'h{i}')
    for header in headers:
        print(f'h{i}: {header.get_text(strip=True)}')

links = soup.find_all('a')
print(f"Total de links encontrados: {len(links)}\n")
for link in links[:10]:  # Exibindo apenas os primeiros 10 links
    href = link.get('href')  # Atributo href
    text = link.get_text(strip=True)  # Texto do link
    print(f"Texto: {text} | URL: {href}")
    
print("Título da página:", soup.title.string)  # Exibe o título da página

