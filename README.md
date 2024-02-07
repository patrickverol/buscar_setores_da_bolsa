<div>
<div align="center">
  <img  src="https://i.imgur.com/7WZ2o8a.png"
    width=100%" >
</div>
<br>
<h1 align="center">
  Shortly - API
</h1>
<div align="center">
  <h3>Ferramentas</h3>
  <img alt="Python" src="https://img.shields.io/badge/Node.js-43853D?style=for-the-badge&logo=node.js&logoColor=white" height="30px"/>  
  <img alt="Pandas" src="https://img.shields.io/badge/Express.js-404D59?style=for-the-badge&logo=express.js&logoColor=white" height="30px"/>
  <img alt="Poetry" src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" height="30px"/>
  <img alt="Selenium" src="https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white" height="30px"/>
  <img alt="Microsoft Excel" src="https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white" height="30px"/>
  <img alt="Power Shell" src="https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white" height="30px"/>
</div>
<br/>
</div>

<div>
    <a href = "https://www.python.org/" target="_blank"><img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white" target="_blank"></a> 
    <a href = "https://pandas.pydata.org/" target="_blank"><img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white" target="_blank"></a>
    <a href = "https://python-poetry.org/docs/"><img src="https://img.shields.io/badge/Poetry-%233B82F6.svg?style=for-the-badge&logo=poetry&logoColor=0B3D8D" target="_blank"></a>
    <a href = "https://www.selenium.dev/pt-br/documentation/"><img src="https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white" target="_blank"></a>
    <a href = "https://www.microsoft.com/pt-br/microsoft-365/excel"><img src="https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white" target="_blank"></a>
    <a href = "https://learn.microsoft.com/pt-br/powershell/scripting/overview?view=powershell-7.4"><img src="https://img.shields.io/badge/Powershell-2CA5E0?style=for-the-badge&logo=powershell&logoColor=white" target="_blank"></a>
</div> 

# Buscar classificação de ações da Bolsa

Este projeto tem o objetivo de buscar a classificação de todas as ações da bolsa de valores do Brasil, através de um web scrapping realizado no site StatusInvest. Desta forma, será possível analisar melhor o valuation das empresas listadas na bolsa, avaliando sua performance com base nos principais indicadores de cada setor e realizando uma análise horizontal comparando-as com seus pares, uma vez que setores diferentes possuem interpretações diferentes dos indicadores.


## Instalação e configuração

  1. Clone o repositório

```bash
  git clone https://github.com/patrickverol/buscar_setores_da_bolsa
  cd buscar_setores_da_bolsa
```
  2. Configure a versão correta do Python com pyenv:

```bash
  pyenv install 3.11.5
  pyenv local 3.11.5
```
  3. Configurar poetry para Python version 3.11.5 e ative o ambiente virtual:

```bash
  poetry env use 3.11.5
  poetry shell
```
  4. Instale as dependências do projeto:

```bash
  poetry install
```
  5. Execute o comando de execucão do programa:

```bash
  task run
```
## Autores

- [@patrickverol](https://github.com/patrickverol)
