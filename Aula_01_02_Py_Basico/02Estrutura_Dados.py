#Listas
#Criando uma lista, use colchetes
lista = [1,2,3]
print(lista)
#Imprindo um elemento da lista
lista = ["Cachorros", "Gatos", 120]
print(lista[2])
#Substituindo um elemento
lista[2] = "Porco"
print(lista)
#removendo um elemento
lista.remove("Gatos")
print(lista)
#Tamanho da lista
print(len(lista))
#Esta na lista
print("raposa" in lista)

#Outras funcões de listas
numeros = [1, 500, 12, -46, 13]
print(max(numeros))
print(min(numeros))
#Add outros elementos
numeros.append(18)
print(numeros)
numeros.extend(["Só existem números na lista", 0])
print(numeros)
#ordenar uma lista
numeros.remove("Só existem números na lista")
numeros=numeros.sort()
print(numeros)

#Tuplas
#para criar uma tupla usa {}
tupla = {"Olá mundo", 12, False, 'P', "12"}

#Dicionarios
#para criar um dicionario usa []
frutas = {10: "Maçã", 25: "Laranja", 35: "Batata"}
frutas[10]
print(frutas)
#mostrar as chaves do dicionarios
print(frutas.keys())
#mostrar os valores do dicionarios
print(frutas.values())
#Verifica se já existe uma chave no dicionario e caso não tenha ele escreve
frutas.setdefault(12, "Limão")
print(frutas)