import json
import pandas as pd
from tqdm import tqdm
import seaborn as sns
import matplotlib.pyplot as plt
import requests

from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter

from google_play_scraper import Sort, reviews, app

import play_scraper
import streamlit as st
import base64
from io import BytesIO


st.write("""
# Play Store Scraping Web App
Encontre aplicativos que precisam de tradução
""")


st.write("""
Cada palavra chave trará 50 aplicativos que serão vasculhados por comentários relevantes
""")
listaPalavras = st.text_input("Digite as palavras chave de busca separadas por virgula")
listaChave = st.text_input("Digite as palavras que sigerem o assunto que estamos buscando", 'translate,traduz,portuguese,traduzir,portugues,português,ingles,inglês,tradução,traduçao,traducao,traducão')
paginas = []
paginasReais = []
palavras = listaPalavras.split(",")
chave = listaChave.split(",")


for i in palavras:
    paginas = paginas + play_scraper.search(i, page=0)


for p in paginas:
    
    if p not in paginasReais:
        paginasReais.append(p)



comentarios = []
for ap in tqdm(paginasReais):
  info = app(ap['app_id'], lang='pt', country='us')
  comentarios.append(info)


titulos = []
coment = []
emailApps = []
linkApps = []

for i in comentarios:
  for a in i['comments']:
    if a is not None:
        if any(word in a for word in chave):
            titulos.append(i['title'])
            coment.append(a)
            emailApps.append(i['developerEmail'])
            linkApps.append(i['url'])


base = pd.DataFrame({'Titulo':titulos,'Comentario':coment,'Email':emailApps,'Link':linkApps})
st.write(base)
st.write('Foram encontrados ', len(base), ' comentários relevantes')



def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1')
    writer.save()
    processed_data = output.getvalue()
    return processed_data


def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    val = to_excel(df)
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="extract.csv">Download csv file</a>'


st.markdown(get_table_download_link(base), unsafe_allow_html=True)




