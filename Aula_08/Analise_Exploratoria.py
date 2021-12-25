#importando as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
from pandas.core import groupby
from pandas.core.indexes.base import Index
plt.style.use("seaborn")
#Criando um DataFrame
df = pd.read_excel("\OneDrive\Área de Trabalho\Python\Python e Pandas\AdventureWorks.xlsx", error_bad_lines = False, sep = ";")
#Visualisando as 5 primeiras linhas
df.head()
#Quantidade de linhas e colunas
df.shepe()
#Verificando os tipos de dados
df.dtypes
#Qual a Receita toral
df["Valor Venda"].sum()
#Qual o custo total
df["Custo"] = df["Custo Unitário"].mul(df["Quantidade"]) #Criando a coluna custo
df.head(1)
round(df["Custo"].sum(), 2)
#Achando o lucro total
df["Lucro"] = df["Valor Venda"] - df["Custo"]
df.head(1)
#Lucro total
round(df["Lucro"].sum(), 2)
#Criando uma coluna com o total de dias para enviar o produto
df["TempoEnvio"] = df["Data Envio"] - df["Data Venda"]
df.head(1)
#Extraindo apenas os dias
df["TempoEnvio"] = (df["Data Envio"] - df["Data Venda"]).dt.days
df.head(1)
#Verificando o tipo de coluna TempoEnvio
df["TempoEnvio"].dtype
#Média do tempo de envio por marca
df.groupby("Marca")["TempoEnvio"].mean()
#verificando valores faltando
df.isnull().sum()
#Agrupar por ano e marca
df.groupby([df["Data Venda"].dt.year, "Marca"])["Lucro"].sum()
pd.options.display.float_format = '{:20,.2f}'.format
#Redetando o index
lucro_ano = df.groupby([df["Data Venda"].dt.year, "Marca"])["Lucro"].sum().reset_index()
#Qual o total de produtos vendidos
df.groupby("Produtos")["Quantidade"].sum().sort_values(ascending = False)
#Grafico total de produtos vendidos
df.groupby("Produtos")["Quantidade"].sum().sort_values(ascending= True).plot.barh("Total produtos vendidos")
plt.xlabel("Total")
plt.ylabel("Produtos");
#Lucro por ano
df.groupby(df["Data Vendas"].dt.year)["Lucro"].sum().plot.bar(title = "Lucro X Ano")
plt.xlabel("Ano")
plt.ylabel("Receita")
df.groupby(df["Data Vendas"].dt.year)["Lucro"].sum()
#Selecioando apenas as vendas de 2009
df_2009 = df[df["Data Vanda"].dt.year == 2009]
df_2009.head()
df_2009.groupby(df_2009["Data Venda"].dt.month)["Lucro"].sum().plot(title = "Lucro X Mês")
plt.xlabel("Mês")
plt.ylabel("Lucro")
plt.xticks(rotation = 'horizontal');
#
df_2009.groupby("Marca")["Lucro"].sum().plot.bar(title = "Lucro X Marca")
plt.xlabel("Marca")
plt.ylabel("Lucro")
plt.xticks(rotation = 'horizontal');
#
df_2009.groupby("Classe")["Lucro"].sum().plot.bar(title = "Lucro X Classe")
plt.xlabel("Classe")
plt.ylabel("Lucro")
plt.xticks(rotation = 'horizontal')
#
df["TempoEnvio"].describe()
#Gráfico de Boxplot
plt.boxplot(df["TempoEnvio"]);
#Histograma
plt.hist(df["TempoEnvio"]);
#Tempo minimo de envio
df["TempoEnvio"].min()
#Tempo maximo de envio
df["TempoEnvio"].max()
#Identificando o Outliter
df[df["TempoEnvio"] == 20]
#Criando um arquivo CSV
df.to_csv("df_vendas_novo.csv", Index = False)