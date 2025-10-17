import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.amazon_page import AmazonPage
import logging
import time

logging.basicConfig(filename='logs/automacao.log', level=logging.INFO, format='%(asctime)s - %(message)s')

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.amazon.com.br")

pagina = AmazonPage(driver)

# Dom Casmurro
pagina.buscar_livro("Dom Casmurro")
logging.info("Buscando Dom Casmurro")
time.sleep(2)
pagina.clicar_primeiro_resultado()
logging.info("Clicando no primeiro resultado de Dom Casmurro")
time.sleep(2)
pagina.adicionar_ao_carrinho()
logging.info("Adicionando Dom Casmurro ao carrinho")
time.sleep(2)

# Voltar para a home
driver.get("https://www.amazon.com.br")

# O Pequeno Príncipe
pagina.buscar_livro("O Pequeno Príncipe")
logging.info("Buscando O Pequeno Príncipe")
time.sleep(2)
pagina.clicar_primeiro_resultado()
logging.info("Clicando no primeiro resultado de O Pequeno Príncipe")
time.sleep(2)
pagina.adicionar_ao_carrinho()
logging.info("Adicionando O Pequeno Príncipe ao carrinho")
time.sleep(2)

# Abrir o carrinho
pagina.abrir_carrinho()
logging.info("Abrindo o carrinho para visualizar os itens")
time.sleep(5)

driver.quit()
