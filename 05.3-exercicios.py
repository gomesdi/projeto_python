# # Exercícios

# # Exercício 1
# # Crie uma lista contendo os números de 1 a 10 elevados ao quadrado.

# numeros = [numero **2 for numero in range (1,11)]

# print(numeros)

# # Exercício 2
# # Dada a lista:

# # numeros = [3, 8, 11, 20, 25, 30]
# # Crie uma nova lista contendo apenas os números maiores que 10.

# numeros = [3, 8, 11, 20, 25, 30]

# numeros_maiores = [
#     numero 
#     for numero in numeros
#     if numero > 10
# ]

# print(numeros_maiores)


# # Exercício 3
# # Dada a lista:

# # nomes = ["ana", "bruno", "carla"]
# # Crie uma nova lista com os nomes em letras maiúsculas.

# nomes = ["ana", "bruno", "carla"]

# nome_maiusculo = [nome.upper() for nome in nomes]

# print(nome_maiusculo)

# # Exercício 4
# # Dada a lista:

# # numeros = [1, 2, 3, 4, 5, 6]
# # Crie um dicionário no formato:

# # {
# #     1: "ímpar",
# #     2: "par",
# #     3: "ímpar",
# #     4: "par",
# #     5: "ímpar",
# #     6: "par"
# # }

# numeros = [1, 2, 3, 4, 5, 6]

# numeros_classificados = {
#     numero: "par" if numero % 2 == 0
#     else "ímpar"
#     for numero in numeros
# }

# print(numeros_classificados)

# # Exercício 5
# # Dado o dicionário:

# # produtos = {
# #     "caneta": 2,
# #     "caderno": 15,
# #     "mochila": 120
# # }
# # Crie um novo dicionário contendo apenas produtos com preço maior que 10.

# produtos = {
#     "caneta": 2,
#     "caderno": 15,
#     "mochila": 120
# }

# produtos_maiores = {
#     produto: valor 
#     for produto, valor in produtos.items()
#     if valor > 10
# }

# print(produtos_maiores)