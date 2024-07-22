# Importação de bibliotecas

# Desativar warnings
import warnings
warnings.filterwarnings("ignore")

# Biblioteca para trabalhar a base de dados
import pandas as pd
import os
import requests
from bs4 import BeautifulSoup

# Importando Steps
from step_download import baixar_planilha
from step_read import ler_planilha

# Configurações do request
headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }

# Funções de busca dos setores
def buscar_setores(df: pd.DataFrame) -> pd.DataFrame:
    
    # Pesquisando todas as ações
    for linha, item in enumerate(df["TICKER"]):

        # URL do arquivo que você deseja baixar
        url = f"https://statusinvest.com.br/acoes/{item}"

        response = requests.get(url, headers=headers)

        if response.status_code == 200:

            soup = BeautifulSoup(response.text, 'html.parser')
            results = soup.find_all("a", class_="white-text d-flex")
            data = []

            for result in results:

                value = result.find("strong", class_="value").text
                data.append(value)

        df.loc[linha, "SETOR"] = data[0]
        df.loc[linha, "SUBSETOR"] = data[1]
        df.loc[linha, "SEGMENTO"] = data[2]

        if __name__ == "__main__":
            print(
                linha,
                item,
                df.loc[linha, "SETOR"],
                df.loc[linha, "SUBSETOR"],
                df.loc[linha, "SEGMENTO"],
            )

    return df

if __name__ == "__main__":
    
    baixar_planilha()
    df = ler_planilha()
    new_df = buscar_setores(df)

    # Exportando o arquivo final
    work_path = os.getcwd()
    os.chdir(work_path)
    df.to_excel("Analise_Fundamentalista_BR.xlsx", index=False)