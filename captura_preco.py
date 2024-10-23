import requests
from bs4 import BeautifulSoup
import os


#variável que pega o URL que deseja monitorar:

def armazena_link():

    caminho = r'C:\Users\GuiMo\Downloads\monitoramento'
    arquivo = caminho + r'\link_monitoramento.txt'

    #Verifica se arquivo da planilha já existe, se ele não existir, o cria na pasta que também é verificada e criada se não existir.
    if os.path.exists(arquivo):
        with open(arquivo, "r") as file:
            link = file.read().strip()
    else:
        link = input("Insira o link do produto que você quer monitorar: ").strip()

        if not os.path.exists(caminho):
            os.makedirs(caminho)

        with open(arquivo, "w") as file:
            file.write(link)
        print(f'Link salvo pra monitoramentos futuros: {link}')

    return link

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}



response = requests.get(armazena_link(), headers=headers)
html = response.text

soup = BeautifulSoup(html, 'html.parser')


#Loop que recolhe o valor do produto, sem os descontos.

def captura_preco():

    #Variável que localiza onde fica o valor do produto
    if "kabum.com.br" in armazena_link():
        preco_produto = soup.find_all('b', {'class': 'regularPrice'})
        for price in preco_produto:
            price = price.text
            new_price = price.replace("R$", "").replace(",", ".")

            return float(new_price)

    if "mercadolivre.com.br" in armazena_link():
        preco_produto = soup.find_all('span', {'class': 'andes-money-amount__fraction'})
        for price in preco_produto[1]:
            price = price.text
            return float(price)


captura_preco()








