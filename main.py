#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importação de bibliotecas

# Biblotecas para importar o ChromeDriver e verificar a versão
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Bibliotecas para utilizar os comandos Keys e By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Biblioteca para trabalhar a base de dados
import pandas as pd
import numpy as np
import os
import time


# In[9]:


# criar o navegador
servico = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=servico)


# In[10]:


# entrar no Status invest
nav.get("https://statusinvest.com.br/")
time.sleep(1)


# In[11]:


nav.find_element(By.XPATH, '//*[@id="main-nav-nav"]/div/div/div/ul/li[4]/a').send_keys(Keys.ENTER)
time.sleep(1)


# In[12]:


nav.find_element(By.XPATH, '//*[@id="acaoDropdown"]/li[2]/a').send_keys(Keys.ENTER)
time.sleep(1)


# In[13]:


nav.find_element(By.XPATH, '//*[@id="main-2"]/div[3]/div/div/div/button[2]').send_keys(Keys.ENTER)
time.sleep(1)


# In[14]:


nav.find_element(By.XPATH, '//*[@id="main-2"]/div[4]/div/div[1]/div[2]/a').click()
time.sleep(1)


# In[15]:


caminho = r'C:\Users\PICHAU\Downloads'
os.chdir(caminho)
df = pd.read_csv('statusinvest-busca-avancada.csv', sep=';')
display(df)


# In[16]:


df.info()


# In[29]:


pip install tqdm


# In[41]:


from tqdm.notebook import tqdm_notebook


# In[70]:


pbar = tqdm_notebook(total=len(new_df['TICKER']), desc='Progress:')

for linha, item in enumerate(new_df['TICKER']):
    pbar.update()
    # entrar no Status invest
    nav.get("https://statusinvest.com.br/")
    time.sleep(3)
    nav.find_element(By.XPATH, '//*[@id="main-nav-nav"]/div/div/div/ul/li[2]/a/i').click()
    time.sleep(2)
    nav.find_element(By.XPATH, '//*[@id="main-search"]/div[1]/span[1]/input[2]').send_keys(item, Keys.ENTER)
    time.sleep(5)
    href = nav.find_element(By.XPATH, '//*[@id="main-search"]/div[2]/div/div/a').click()
    time.sleep(3)
    new_df.loc[linha, 'SETOR'] = nav.find_element(By.XPATH, '//*[@id="company-section"]/div[1]/div/div[3]/div/div[1]/div/div/div/a/strong').text
    time.sleep(1)
    new_df.loc[linha, 'SUBSETOR'] = nav.find_element(By.XPATH, '//*[@id="company-section"]/div[1]/div/div[3]/div/div[2]/div/div/div/a/strong').text
    time.sleep(1)
    new_df.loc[linha, 'SEGMENTO'] = nav.find_element(By.XPATH, '//*[@id="company-section"]/div[1]/div/div[3]/div/div[3]/div/div/div/a/strong').text
    time.sleep(1)


# In[8]:


df.to_excel('Analise_Fundamentalista_BR.xlsx', index=False)


# In[9]:


df = pd.read_excel('Analise_Fundamentalista_BR.xlsx')


# In[10]:


display(df)


# In[ ]:




