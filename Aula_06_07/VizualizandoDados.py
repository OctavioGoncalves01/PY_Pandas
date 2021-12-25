#Importando a biblioteca
import pandas as pd
from pandas.core import groupby

df1 = pd.read_excel("Aracaju.xlsx")
df2 = pd.read_excel("Fortaleza.xlsx")
df3 = pd.read_excel("Natal.xlsx")
df4 = pd.read_excel("Recife.xlsx")
df5 = pd.read_excel("Salvador.xlsx")

#Juntando todas os arquivos
df = pd.concat([df1, df2, df3, df4, df5])

#
df["LojaID"].value_counts(ascending=False)

#Gerando um Grafico
df["LojaID"].value_counts(ascending= False).plot.bar()

#Gerando um Grafico de barras horizontais
df["LojaID"].value_counts(ascending= False).plot.barh()

#Gerando um Grafico de barras horizontais do maior para o menor
df["LojaID"].value_counts(ascending= True).plot.barh();

#Grafico de Pizza por ano
#df.groupby(df["Data"].dt.year)["Receita"].sum().plot.pie()

#Vendas por cidade
df["Cidade"].value_counts()

#Add um titulo e alterando nome dos eixos
import matplotlib.pyplot as plt
df["Cidade"].value_counts().plot.bar(title = "Total de Vandas por Cidade")
plt.xlabel("Cidade")
plt.ylabel("Total Vendas")

#Mudando a cor
#df["Cidade"].value_counts().plot.bar()(title = "Total de Vandas por Cidade", color = "pink")
#plt.xlabel("Cidade")
#plt.ylabel("Total Vendas")

#Alterando o estilo
#plt.style.use("ggplot")
#df.groupby(df["mes_vendas"] ["Qtde"].sum.plot(title = "Total de Produtos vendidos por mês")
#plt.plt.xlabel("Mês")
#plt.plt.ylabel("Total Produtos Vendidos")
#plt.plt.legend()

#Selecionando apneas as vendas de 2019
df.groupby(df["mes_vendas"])["Qtde"].sum()
df_2019 = df[df["Ano_Venda"] == 2019]

#Total produtos vendidos por mes
df_2019.groupby(df_2019["mes_vendas"])["Qtde"].sum().plt.plot(marker = "*")
plt.plt.xlabel("Mês")
plt.plt.ylabel("Total Produtos vendidos");
plt.legend();

#Histograma
plt.plt.hist(df["Qtde"], color = "Green");

#Grafico de dispersão
plt.plt.scatter(x = df_2019["dia_veda"], y = df_2019["Receit"]);

#Salvando em png
df_2019.groupby(df_2019["mes_vendas"])["Qtde"].sum().plt.plot(marker = "*")
plt.plt.xlabel("Mês")
plt.plt.ylabel("Total Produtos vendidos");
plt.legend();
plt.savefig("Grafico QTDE x Mes.png")