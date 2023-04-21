# ac3-web-mining-impacta

## Integrantes do trabalho

- Arthur Vinicius Santos Silva RA:1903665
- Carolina Gabrielle Castro Vieira RA:1900127

## Link do projeto

![Captura de Tela 2023-04-21 às 09 46 24](https://user-images.githubusercontent.com/53263896/233639632-52223d4e-1e92-4b61-8006-0959ea3a1547.png)

[AC3 - Extração dados Nuuvem](https://thuurzz-ac3-web-mining-impacta-script-josyxq.streamlit.app/)

## Como rodar o projeto:

Instalar requerimentos

```shell
pip install -r requirements.txt
```

Habilitar o modo Shell do Scrapy para testes:

```shell
scrapy shell
```

comando para executar spider e salvar o retorno:

```shell
# scrapy crawl <<nome-spider>> -O nome-do-arquivo.tipo-arquivo(csv,json,etc...)
scrapy crawl promocoes-jogos -O ../../../../../0_bases_originais/original.csv
```

## Rodar o streamlit

```
streamlit run script.py
```
