# Exercício 1 — Lista
# Crie uma lista com cinco números e:

# Mostre o primeiro número;
# Mostre o último número;
# Adicione um novo número;
# Remova um número;
# Mostre a quantidade de elementos.

numeros = [1, 2, 3, 4, 5]

print(numeros[0])
print(numeros[-1])

numeros.append(6)
print(numeros)

numeros.remove(3)
print(numeros)

print(len(numeros))

# Exercício 2 — Dicionário
# Crie um dicionário representando um produto:

# produto = {
#     "nome": "Teclado",
#     "preco": 150,
#     "estoque": 10,
# }
# Depois:

# Mostre o nome do produto;
# Altere o preço;
# Adicione a chave "marca";
# Percorra o dicionário mostrando chave e valor.

produto = {
    "nome_produto": "notebook",
    "preco_produto": 2500.00,
    "estoque": 15,
}

print(produto["nome_produto"])

produto["preco_produto"] = 2200.00
print(produto["preco_produto"])

produto["marca"] = "lenovo"

print(produto)

for chave, valor in produto.items():
    print(f"{chave}: {valor}")

# Exercício 3 — Set
# Dada a lista:

numeros = [1, 2, 2, 3, 4, 4, 5, 5, 5]
# Converta-a para um set para eliminar os valores repetidos.

set_numeros = set(numeros)

print(set_numeros)

# Exercício 4 — Estrutura combinada
# Crie um dicionário de aluno contendo:

# Nome;
# Idade;
# Lista de notas;
# Tupla com as disciplinas;
# Set com as linguagens de programação conhecidas.
# Depois, mostre cada informação na tela.

alunos = {
    "nome": "Diego",
    "idade": 42, 
    "notas": [8.8, 9.2, 10.0],
    "disciplinas": ("Python", "Django"),
    "linguagens": {"HTML", "CSS", "Js"},
}

print(alunos["nome"])
print(alunos["idade"])
print(alunos["notas"])
print(alunos["disciplinas"])
print(alunos["linguagens"])

for chave, valor in alunos.items():
    print(f"{chave}: {valor}")