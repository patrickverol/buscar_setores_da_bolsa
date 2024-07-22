# importação de bibliotecas

# Biblotecas para importar o ChromeDriver e verificar a versão
import time

# Biblioteca para trabalhar a base de dados
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Bibliotecas para utilizar os comandos Keys e By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# criar o navegador
servico = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
nav = webdriver.Chrome(service=servico, options=options)


# Definindo função de busca
def buscar_elemento(classe: str):
    elements = nav.find_elements(By.CLASS_NAME, classe)
    for element in elements:
        try:
            element.click()
        except:
            pass


# Definindo a função de da baixar a planilha
def baixar_planilha():
    # entrar no Status invest
    nav.get("https://statusinvest.com.br/")

    nav.implicitly_wait(10)  # seconds
    buscar_elemento("btn-close")

    wait = WebDriverWait(nav, 5)

    # Clicando em Ações
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="main-nav-nav"]/div/div/div/ul/li[5]/a/i')
        )
    )
    nav.find_element(
        By.XPATH, '//*[@id="main-nav-nav"]/div/div/div/ul/li[5]/a/i'
    ).click()

    # Clicando em Busca Avançada
    wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="acaoDropdown"]/li[2]/a'))
    )
    nav.find_element(By.XPATH, '//*[@id="acaoDropdown"]/li[2]/a').click()

    # Clicando em Buscar
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="main-2"]/div[3]/div/div/div/button[2]')
        )
    )
    nav.find_element(By.XPATH, '//*[@id="main-2"]/div[3]/div/div/div/button[2]').click()

    # Clicando em Download
    time.sleep(3)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="main-2"]/div[4]/div/div[1]/div[2]/a/span')
        )
    )
    nav.find_element(
        By.XPATH, '//*[@id="main-2"]/div[4]/div/div[1]/div[2]/a/span'
    ).click()
    time.sleep(3)