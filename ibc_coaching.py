from bs4 import BeautifulSoup as bs
from pathlib import Path
import requests as req
import pandas as pd

frases = []

#Caminho do arquivo que irá armazenar as frases coletadas
file_path = Path.cwd()

#Instanciando Dataframe
dataframe = pd.read_excel(f'{file_path}/frases.xlsx')

novo_df = pd.DataFrame()

#Inicio do scrap
try:
    #site que será scrapado
    url = 'https://www.ibccoaching.com.br/portal/lideranca-e-motivacao/confira-frases-motivacionais-famosas-inspiradoras/'
    print(f'Iniciando o scrap do link {url}')
    #lib que faz as requisições web
    request = req.get(url=url)

    #Iniciando o beautifulsoup
    soup = bs(request.content, 'html.parser')

    for texto in soup.find_all('b'):
        frases.append(texto.text)

    for citacao in soup.find_all('li'):
        for texto in citacao.find_all('span'):
            frases.append(texto.text)
            
    print(f'Terminando o link {url}')
    print(f'Contando... após a {url} passamos a ter \033[1;34m{frases.__len__()}\033[m frases salvas')

    novo_df['Frases'] = frases
    novo_df['Categorias'] = 'frases-motivacionais-inspiradoras'

    dataframe = dataframe.append(novo_df)
    dataframe.to_excel(f'{file_path}/frases.xlsx', header='frases', index=False)
    print('Arquivo criado com sucesso')

except:
    print('Deu ruim')