import os
import pandas as pd

def ler_planilha() -> pd.DataFrame:
    
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

    return df