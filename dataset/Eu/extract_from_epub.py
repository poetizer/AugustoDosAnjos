import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

book = epub.read_epub('Eu.epub')
count = 0
raw = []
poemas = {}

for item in book.get_items():
    if item.get_type() == ebooklib.ITEM_DOCUMENT:
        if count > 3:
            soup = BeautifulSoup(item.get_content(), 'html.parser')
            extract = soup.get_text().split('\n')
            raw.append(soup.get_text())
            titulo = extract[4]
            corpo = extract[5:]
            poemas[titulo] = corpo
        count += 1

file = open('eu - augusto dos anjos.txt', 'w')

file.write('\n'.join(raw))
print(poemas)
