# importação de bibliotecas

# Biblotecas para importar o ChromeDriver e verificar a versão
import os
import random
import time

# Biblioteca para trabalhar a base de dados
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Bibliotecas para utilizar os comandos Keys e By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# criar o navegador
servico = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=servico)
nav.maximize_window()


# Definindo função de busca
def buscar_elemento(classe: str):
    elements = nav.find_elements(By.CLASS_NAME, classe)
    for element in elements:
        try:
            element.click()
        except:
            pass


# Definindo a função de simulador humano
def simulador_humano():
    time.sleep(random.randint(0, 1))


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

def ler_planilha():
    # Lendo o arquivo baixado
    downloads_path = os.path.expanduser("~/Downloads")

    # Verifique se o diretório existe
    if os.path.exists(downloads_path):
        # Navegue até a pasta de Downloads
        os.chdir(downloads_path)
        # Faça alguma coisa dentro da pasta de Downloads (exemplo: listar arquivos)
        df = pd.read_csv("statusinvest-busca-avancada.csv", sep=";")


    else:
        print("O diretório de Downloads não existe neste sistema.")

# Criando a nova planilha
new_df = pd.DataFrame()

# Pesquisando todas as ações
for linha, item in enumerate(df["TICKER"]):
    try:
        # entrar no Status invest
        nav.get("https://statusinvest.com.br/")

        simulador_humano()
        nav.find_element(
            By.XPATH, '//*[@id="main-nav-nav"]/div/div/div/ul/li[2]/a/i'
        ).click()
        # time.sleep(2)
        nav.find_element(
            By.XPATH, '//*[@id="main-search"]/div[1]/span[1]/input[2]'
        ).send_keys(item, Keys.ENTER)
        # time.sleep(5)
        href = nav.find_element(
            By.XPATH, '//*[@id="main-search"]/div[2]/div/div/a'
        ).click()
        # time.sleep(3)
        df.loc[linha, "SETOR"] = nav.find_element(
            By.XPATH,
            '//*[@id="company-section"]/div[1]/div/div[3]/div/div[1]/div/div/div/a/strong',
        ).text
        # time.sleep(1)
        df.loc[linha, "SUBSETOR"] = nav.find_element(
            By.XPATH,
            '//*[@id="company-section"]/div[1]/div/div[3]/div/div[2]/div/div/div/a/strong',
        ).text
        # time.sleep(1)
        df.loc[linha, "SEGMENTO"] = nav.find_element(
            By.XPATH,
            '//*[@id="company-section"]/div[1]/div/div[3]/div/div[3]/div/div/div/a/strong',
        ).text
        # time.sleep(1)

        if __name__ == "__main__":
            print(
                linha,
                item,
                df.loc[linha, "SETOR"],
                df.loc[linha, "SUBSETOR"],
                df.loc[linha, "SEGMENTO"],
            )

    except:
        # Exportando o arquivo final
        df.to_excel("Analise_Fundamentalista_BR.xlsx", index=False)

# Exportando o arquivo final
work_path = os.getcwd()
os.chdir(work_path)
df.to_excel("Analise_Fundamentalista_BR.xlsx", index=False)
