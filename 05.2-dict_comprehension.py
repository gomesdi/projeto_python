# # Dict comprehension

# numeros = [1, 2, 3, 4, 5]

# quadrados = {
#     numero: numero ** 2
#     for numero in numeros
# }

# print(quadrados)

# # Criando um dicionário a partir de duas listas

# nomes = ["Ana", "Bruno", "Carlos"]
# idades = [20, 25, 30]

# # sem dict comprehension
# pessoas = dict(zip(nomes, idades))

# print(pessoas)


# # com dict comprehension
# pessoas = {
#     nome: idade
#     for nome, idade in zip(nomes, idades)
# }

# print(pessoas)


# # Dict comprehension com condição

# numeros = range (1, 11)

# quadrados_pares = {
#     numero: numero ** 2
#     for numero in numeros
#     if numero % 2 == 0
# }

# print(quadrados_pares)

# #Dict comprehension com if e else

# numeros = [1, 2, 3, 4, 5]

# classificacao = {
#     numero: "par" if numero % 2 == 0 else "ímpar"
#     for numero in numeros
# }

# print(classificacao)

# #Transformando valores de um dicionário

# precos = {
#     "arroz": 20,
#     "feijão": 8, 
#     "macarrão": 5
# }

# precos_com_desconto = {
#     produto: preco * 0.9
#     for produto, preco in precos.items()
# }

# print(precos_com_desconto)

# #Filtrando um dicionário

# notas = {
#     "Ana": 8,
#     "Bruno": 5,
#     "Carlos": 9,
#     "Daniela": 6
# }

# aprovados = {
#     aluno: nota
#     for aluno, nota in notas.items()
#     if nota >= 7
# }

# print(aprovados)





