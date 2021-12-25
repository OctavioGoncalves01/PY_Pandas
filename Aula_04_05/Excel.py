import pandas as pd
df1 = pd.read_excel("Aracaju.xlsx")
df2 = pd.read_excel("Fortaleza.xlsx")
df3 = pd.read_excel("Natal.xlsx")
df4 = pd.read_excel("Recife.xlsx")
df5 = pd.read_excel("Salvador.xlsx")

#Juntando todas os arquivos
df = pd.concat([df1, df2, df3, df4, df5])
#Exibindo as 5 primeiras linhas
df.head()
#Exibindo as 5 últimas linhas
df.tail()
#Verificando o tipo de dado da coluna LojaID
df.dtypes()
#Alterando o tipo de dado da coluna LojaID
df["LojaID"] = df["LojaID"].astype("object")
df.dtypes()
#Consultando linhas com valores faltando
df.isnull().sun()
#Substitundo os valores pela media
df["Vendas"].fillna(df["Vendas"].mean, inplace = True)#Vai mudar na memoria
df.isnull().sum()
#subustituir por Zero
df["Vendas"].fillna(df["Vendas"].mean(), inplace = True)
#apagando os valores nulos
df.dropna(inplace= True)
#apagando as linhas com valores nulos com base em uma coluna
df.dropna(subset=["Vendas"], inplace= True)
#removendolinhas com valores faltantes de todas as colunas
df.dropna(how= "all", inplace= True)
#Criando novas colunas
df["Receita"] = df["Vendas"].mul(df["qtde"])
df["REceita/Vendas"] = df["Receita"] / df["Vendas"]
df.head()
#Retornar a maior e menor c=receita
df["Receita"].max()
df["Receita"].min()
#Retornar os maiores e menores valores com susas linhas
df.nlargest(3, "Receita")
df.nsmallest(3, "Receita")
#Agrupamento por cidade
df.groupby("Cidade")["Receita"].sum()
#Ordenado o conjunto de dados
df.sort_values("Receita", ascending= False).head(10)

