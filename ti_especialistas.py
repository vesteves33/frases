from bs4 import BeautifulSoup as bs
from pathlib import Path
import requests as req

frases = []

#Caminho do arquivo que irá armazenar as frases coletadas
file_path = Path.cwd()

#Inicio do scrap
try:
    #site que será scrapado
    url = 'https://www.tiespecialistas.com.br/60-frases-motivacionais-escolha-uma-delas/'
    print(f'Iniciando o scrap do link {url}')
    #lib que faz as requisições web
    request = req.get(url=url)

    #Iniciando o beautifulsoup
    soup = bs(request.content, 'html.parser')

    for texto in soup.find_all('li'):
        frases.append(texto.text)

            
    print(f'Terminando o link {url}')
    print(f'Contando... após a {url} passamos a ter \033[1;34m{frases.__len__()}\033[m frases salvas')
        
except:
    print('Deu ruim')









