from bs4 import BeautifulSoup as bs
from pathlib import Path
import requests as req
import pandas as pd

frases = []

#Caminho do arquivo que irá armazenar as frases coletadas
file_path = Path.cwd()

#Instanciando dataframe para conversão em arquivo
dataframe = pd.read_excel(f'{file_path}/frases.xlsx')

new_df = pd.DataFrame()

#Inicio do scrap
try:
    #site que será scrapado
    url = 'https://neilpatel.com/br/blog/frases-motivacionais/'
    print(f'Iniciando o scrap do link {url}')
    #lib que faz as requisições web
    request = req.get(url=url)

    #Iniciando o beautifulsoup
    soup = bs(request.content, 'html.parser')

    for texto in soup.find_all('em'):
        frases.append(texto.text)
            
    print(f'Terminando o link {url}')
    print(f'Contando... após a {url} passamos a ter \033[1;34m{frases.__len__()}\033[m frases salvas')
        
    new_df['Frases'] = frases
    new_df['Categorias'] = 'frases-motivacionais'

    dataframe = dataframe.append(new_df)
    
    dataframe.to_excel(f'{file_path}/frases.xlsx', header='frases', index=False)
    print('Arquivo criado com sucesso')

except:
    print('Deu ruim')