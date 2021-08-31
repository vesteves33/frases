from bs4 import BeautifulSoup as bs
from pathlib import Path
import requests as req
import time
import pandas as pd

#Categorias que serão pesquisadas
categorias = ['frases-filosoficas-de-reflexao', 
              'frases-de-bom-dia-com-sabedoria', 
              'frases-de-mudancas-sao-necessarias', 
              'frases-de-metas', 
              'frases-positivas', 
              'frases-de-esperanca',
              'frases-de-autoajuda', 
              'frases-de-motivacao', 
              'frases-de-autoestima',
              'frases-de-positividade',
              'frases-de-otimismo',
              'frases-de-superacao' 
              ]
frases = []

#Caminho do arquivo que irá armazenar as frases coletadas
file_path = Path.cwd()

#Iniciando dataframe
dataframe = pd.read_excel(f'{file_path}/frases.xlsx')

new_df = pd.DataFrame()

#Inicio do scrap
try:
    for item in categorias:
        #site que será scrapado
        url = f'https://www.frasesdobem.com.br/{item}'
        print(f'Iniciando o scrap do link {url}')

        #lib que faz as requisições web
        request = req.get(url=url)

        #Iniciando o beautifulsoup
        soup = bs(request.content, 'html.parser')


        for citacao in soup.find_all(class_='blockquote'):
            for texto in citacao.find_all('p'):
                frases.append(texto.text)       
        
        for texto in soup.find_all('p', class_='frase'):
            frases.append(texto.text)

        for texto in soup.find_all('p', itemprop='text'):
            frases.append(texto.text)
        
        print(f'Terminando o link {url}')
        print(f'Contando... após a {url} passamos a ter \033[;94m{frases.__len__()}\033[m frases salvas')
          
        time.sleep(5)
    new_df['Frases'] = frases
    

    dataframe = dataframe.append(new_df)
    print(dataframe)

    #dataframe.to_excel(f'{file_path}/frases.xlsx', header='frases', index=False)
    #print('Arquivo criado com sucesso')


except:
    print('Deu ruim')


