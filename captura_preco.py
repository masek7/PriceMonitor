import requests
from bs4 import BeautifulSoup


#variáveis que pegam os URL que estou monitorando:
url = 'https://www.kabum.com.br/produto/471916/monitor-gamer-curvo-kbm-gaming-mg210-23-6-180hz-full-hd-1ms-displayport-e-hdmi-adaptive-sync-ajuste-de-angulo-kgmg21023pt'

response = requests.get(url)

html = response.text


soup = BeautifulSoup(html, 'html.parser')



#Variável que localiza onde fica o valor do produto
preco_produto = soup.find_all('b', {'class': 'regularPrice'})


#Loop que recolhe o valor do produto, sem o desconto do pix
def captura_preco(produto):
    for price in produto:
        price = price.text
        new_price = price.replace("R$","").replace(",",".")
        return float(new_price)



captura_preco(preco_produto)








