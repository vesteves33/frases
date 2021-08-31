from bs4 import BeautifulSoup as bs
from pathlib import Path
from numpy import empty
import requests as req
import pandas as pd

frases = []

#Caminho do arquivo que irá armazenar as frases coletadas
file_path = Path.cwd()

#Instanciando dataframe para conversão em arquivo
dataframe = pd.DataFrame()

#Inicio do scrap
try:
    #site que será scrapado
    url = f'https://blog.malupires.com.br/70-frases-motivacionais-curtas-para-levantar-o-astral/'
    print(f'Iniciando o scrap do link {url}')
    #lib que faz as requisições web
    request = req.get(url=url)

    #Iniciando o beautifulsoup
    soup = bs(request.content, 'html.parser')

    for citacao in soup.find_all('div', class_='entry-content'):
        for texto in citacao.find_all('p'):
            frases.append(texto.text)
        
    print(f'Terminando o link {url}')
    print(f'Contando... após a {url} passamos a ter \033[1;34m{frases.__len__()}\033[m frases salvas')
              
    dataframe['Frases'] = frases
    dataframe['Categorias'] = 'frases-motivacionais-para-levantar-astral'
    
    if dataframe is not empty:
        dataframe.to_excel(f'{file_path}/frases.xlsx', header='frases', index=False)
        print('Arquivo criado com sucesso...')
    
except:
    print('Deu ruim')



