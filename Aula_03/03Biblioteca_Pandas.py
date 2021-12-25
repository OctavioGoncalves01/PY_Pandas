#importando a biblioteca Pandas
from os import sep
import pandas as pd
df = pd.read_csv("C:\Users\octav_jojrcpm\OneDrive\Área de Trabalho\Python\Python e Pandas\datasets\Gapminder.csv", error_bad_lines = False, sep = ";")
#Visualizando as 5 Prinmeiros linhas
df.head()
df = df.rename(columns = {"country" : "Pais", "continentes": "Continente", "year": "Ano", "lifeExp": "ExpectativaVIda", "pop": "PopuTotal", "gdpPerCap": "PIB"})
df.head(10)
#Total de linhas e colunas
df.shape
#Apenas os nomes das colunas
df.columns
#Tipos de dados
df.dtypes
#As ultimas linhas
df.tails(15)
#Retornar as estatisticas dos dados
df.describe()
#Fazer um filtro
df["Continentes"].unique()
oceania = df.loc[df["Continentes"] == "Oceania"]
oceania.head()
#Agrupamento de dados
df.groupby("Continentes")["Pais"].nunique()
df.groupby("Ano")["ExpectativaVIda"].mean()