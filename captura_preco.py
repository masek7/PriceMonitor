import requests
from bs4 import BeautifulSoup


#variável que pega o URL que estou monitorando:

url = 'https://www.kabum.com.br/produto/471916/monitor-gamer-curvo-kbm-gaming-mg210-23-6-180hz-full-hd-1ms-displayport-e-hdmi-adaptive-sync-ajuste-de-angulo-kgmg21023pt'

response = requests.get(url)

html = response.text

soup = BeautifulSoup(html, 'html.parser')

#Loop que recolhe o valor do produto, sem o desconto do pix
def captura_preco():

    #Variável que localiza onde fica o valor do produto
    if "kabum.com.br" in url:
        preco_produto = soup.find_all('b', {'class': 'regularPrice'})
        for price in preco_produto:
            price = price.text
            new_price = price.replace("R$", "").replace(",", ".")
            return float(new_price)


    if "mercadolivre.com.br" in url:
        preco_produto = soup.find_all('span', {'class': 'andes-money-amount__fraction'})
        for price in preco_produto[1]:
            price = price.text
            return float(price)


captura_preco()








