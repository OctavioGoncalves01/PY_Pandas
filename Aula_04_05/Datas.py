import pandas as pd
df1 = pd.read_excel("Aracaju.xlsx",)
df2 = pd.read_excel("Fortaleza.xlsx")
df3 = pd.read_excel("Natal.xlsx")
df4 = pd.read_excel("Recife.xlsx")
df5 = pd.read_excel("Salvador.xlsx")
df = pd.concat([df1, df2, df3, df4, df5])

#Transformando a coluna de datas em int
df["Datas"] = df["Data"].astype("int64")
#Transformando em Data
pd["Data"] = pd.to_datetime(pd["Data"])
#Agrupamento por ano
df.groupby(df["Data"].dt.year)["Receita"].sum()
#Criando uma nova coluna com o ano
df["Ano_Vendas"] = df["Data"].dt.year
#Extraindo o mes e o dia
df["mes_venda"], df["dia_venda"] = (df["Data"].df.month, df["Data"].dt.day)
#Retornando a data mais antiga
df["Data"].min()
#Calculando a diferenca de dias
df["diferenca_dias"] = df["Data"] - df("Data").min()
#Criando a coluna de trimenstre
df["trimenstre_venda"] = df["Data"].dt.quarter
#Filtrando as vendas de 2019 do mes de março
vendas_marco_19 = df.loc[(df["Data"].dt.year == 2019) & (df["Data".dt.month] == 3)]
vendas_marco_19.sample(10)