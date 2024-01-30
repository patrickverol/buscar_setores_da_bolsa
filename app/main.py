# importação de bibliotecas

# Biblotecas para importar o ChromeDriver e verificar a versão
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Bibliotecas para utilizar os comandos Keys e By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Biblioteca para trabalhar a base de dados
import pandas as pd
import numpy as np
import os  
import time
import random

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
    time.sleep(random.randint(0,4))

# Definindo a função de da baixar a planilha
def baixar_planilha():
    # entrar no Status invest
    nav.get("https://statusinvest.com.br/")

    nav.implicitly_wait(10) # seconds
    buscar_elemento('btn-close')

    wait = WebDriverWait(nav, 5)

    # Clicando em Ações
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-nav-nav"]/div/div/div/ul/li[5]/a/i')))
    nav.find_element(By.XPATH, '//*[@id="main-nav-nav"]/div/div/div/ul/li[5]/a/i').click()

    # Clicando em Busca Avançada
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="acaoDropdown"]/li[2]/a')))
    nav.find_element(By.XPATH, '//*[@id="acaoDropdown"]/li[2]/a').click()

    # Clicando em Buscar
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-2"]/div[3]/div/div/div/button[2]')))   
    nav.find_element(By.XPATH, '//*[@id="main-2"]/div[3]/div/div/div/button[2]').click()

    # Clicando em Download
    time.sleep(3)
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-2"]/div[4]/div/div[1]/div[2]/a/span')))
    nav.find_element(By.XPATH, '//*[@id="main-2"]/div[4]/div/div[1]/div[2]/a/span').click()
    time.sleep(3)

baixar_planilha()

# Lendo o arquivo baixado
caminho = r'C:\Users\PICHAU\Downloads'
os.chdir(caminho)
new_df = pd.read_csv('statusinvest-busca-avancada.csv', sep=';')

# Pesquisando todas as ações
for linha, item in enumerate(new_df['TICKER']):
    
    # entrar no Status invest
    nav.get("https://statusinvest.com.br/")

    simulador_humano()
    nav.find_element(By.XPATH, '//*[@id="main-nav-nav"]/div/div/div/ul/li[2]/a/i').click()
    #time.sleep(2)
    nav.find_element(By.XPATH, '//*[@id="main-search"]/div[1]/span[1]/input[2]').send_keys(item, Keys.ENTER)
    #time.sleep(5)
    href = nav.find_element(By.XPATH, '//*[@id="main-search"]/div[2]/div/div/a').click()
    #time.sleep(3)
    new_df.loc[linha, 'SETOR'] = nav.find_element(By.XPATH, '//*[@id="company-section"]/div[1]/div/div[3]/div/div[1]/div/div/div/a/strong').text
    #time.sleep(1)
    new_df.loc[linha, 'SUBSETOR'] = nav.find_element(By.XPATH, '//*[@id="company-section"]/div[1]/div/div[3]/div/div[2]/div/div/div/a/strong').text
    #time.sleep(1)
    new_df.loc[linha, 'SEGMENTO'] = nav.find_element(By.XPATH, '//*[@id="company-section"]/div[1]/div/div[3]/div/div[3]/div/div/div/a/strong').text
    #time.sleep(1)
    print(linha, item, new_df.loc[linha, 'SETOR'], new_df.loc[linha, 'SUBSETOR'], new_df.loc[linha, 'SEGMENTO'])

# Exportando o arquivo final
new_df.to_excel('Analise_Fundamentalista_BR.xlsx', index=False)