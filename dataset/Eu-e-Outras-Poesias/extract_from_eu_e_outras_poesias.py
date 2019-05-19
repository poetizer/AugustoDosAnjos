import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

book = epub.read_epub('Eu e Outras Poesias - Augustos dos Anjos.epub')
count = 0
raw = []
poemas = []


def isTitle(term):
    isTitle = term != ''
    for char in term:
        if not char in 'ABCDEFGHIJKLMNOPQRSTUVXZWYKÍÁÓÚÉÃÇ ':
            isTitle = False
            break

    return isTitle


# Abre o .epub e extrai as seções colocando tudo em um array de linhas.
for item in book.get_items():
    if item.get_type() == ebooklib.ITEM_DOCUMENT:
        if count > 1:
            soup = BeautifulSoup(item.get_content(), 'html.parser')
            extract = soup.get_text().split('\n')
            extract_v2 = list(map(str.strip, extract))
            raw.append(soup.get_text())
            try:
                poemas += extract_v2
            except:
                pass
        count += 1

p = {'Trancrição de Poemas': []}

poemaDaVez = 'Trancrição de Poemas'
c = 0

for verso in poemas:
    if isTitle(verso):
        if not verso in p.keys():
            poemaDaVez = verso
        else:
            poemaDaVez = verso + "_" + str(c)
            c += 1
        p[poemaDaVez] = []
    else:
        p[poemaDaVez].append(verso)

# Processo de remoção de linhas duplas
# Talvez melhorar?
poemas_str = []
for titulo in p.keys():
    poema = [titulo.split('_')[0]] + p[titulo]
    poemas_str += poema

poemas_str2 = []
for i in range(len(poemas_str)-1):
    if not (poemas_str[i] == '' and poemas_str[i+1] != ''):
        poemas_str2.append(poemas_str[i])

poemas_str3 = []
for i in range(len(poemas_str2)-1):
    if not (poemas_str2[i] == '' and poemas_str2[i+1] != ''):
        poemas_str3.append(poemas_str2[i])

poemas_str4 = []
for i in range(len(poemas_str3)-1):
    if not (poemas_str3[i] == '' and poemas_str3[i+1] == ''):
        poemas_str4.append(poemas_str3[i])
# Remoção concluída


file = open('Eu e Outras Poesias - Augustos dos Anjos.txt', 'w')

file.write('\n'.join(poemas_str4))
