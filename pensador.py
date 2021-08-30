from bs4 import BeautifulSoup as bs
from pathlib import Path
import requests as req
import time


categorias = ['mensagens_de_reflexao',
              'frases_de_motivacao',
              'frases_inteligentes',
              'frases_bonitas',
              'frases_de_superacao',
              'autor/sigmund_freud']

frases = []

#Caminho do arquivo que irá armazenar as frases coletadas
file_path = Path.cwd()

#Inicio do scrap
try:
    for item in categorias:
        #site que será scrapado
        url = f'https://www.pensador.com/{item}/'
        print(f'Iniciando o scrap do link {url}')
        #lib que faz as requisições web
        request = req.get(url=url)

        #Iniciando o beautifulsoup
        soup = bs(request.content, 'html.parser')

        for texto in soup.find_all('p', class_='frase '):
            frases.append(texto.text)
            
        print(f'Terminando o link {url}')
        print(f'Contando... após a {url} passamos a ter \033[1;34m{frases.__len__()}\033[m frases salvas')
        
        time.sleep(10)
except:
    print('Deu ruim')