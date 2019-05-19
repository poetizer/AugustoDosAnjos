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


def removeExtraNewLine(poemasStr):
    novoPoemasStr = []
    for i in range(len(poemasStr)-1):
        if not (poemasStr[i] == '' and poemasStr[i+1] != ''):
            novoPoemasStr.append(poemasStr[i])
    return novoPoemasStr


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

mapaDePoemas = {'Trancrição de Poemas': []}

tituloDaVez = 'Trancrição de Poemas'
conflict = 0

for linha in poemas:
    if isTitle(linha):
        if not linha in mapaDePoemas.keys():
            tituloDaVez = linha
        else:  # titulo já existe
            tituloDaVez = linha + "_" + str(conflict)
            conflict += 1
        mapaDePoemas[tituloDaVez] = []
    else:
        mapaDePoemas[tituloDaVez].append(linha)

# Remoção da flag de conflito
poemas_str = []
for titulo in mapaDePoemas.keys():
    poema = [titulo.split('_')[0]] + mapaDePoemas[titulo]
    poemas_str += poema

# Processo de remoção de linhas duplas
poemasSemiClean = removeExtraNewLine(removeExtraNewLine(poemas_str))

poemasClean = []
for i in range(len(poemasSemiClean)-1):
    if not (poemasSemiClean[i] == '' and poemasSemiClean[i+1] == ''):
        poemasClean.append(poemasSemiClean[i])
# Remoção concluída


file = open('Eu e Outras Poesias - Augustos dos Anjos.txt', 'w')

file.write('\n'.join(poemasClean))
