# Listas: Armazena valores em uma sequência ordenada.

# As listas são:
#   - Ordenadas;
#   - Mutáveis, ou seja, podem ser alteradas;
#   - Permitem valores repetidos;
#   - Acessadas por índices.

frutas = ["maça", "Banana", "laranja"]

print(frutas)

# Alteração

frutas[1] = "uva"

print(frutas[1])
print(frutas)

# Adicionando no final da fila (.append())

frutas = ["maçã", "banana"]

frutas.append("laranja")

print(frutas)

# Adicionando em posição específica (.insert())

frutas = ["maça", "laranja"]
frutas.insert(1, "banana")
print(frutas)

# Adicionando vários elementos (.extend())

frutas = ["maça", "banana"]

frutas.extend(["laranja", "uva"])

print(frutas)

# Removendo elementos (.remove())

frutas = ["maçã", "banana", "laranja"]

frutas.remove("banana")

print(frutas)

# Removendo pelo índice e retorna o item removido (.pop())

frutas = ["maça", "banana", "laranja"]

fruta_removida = frutas.pop(1) # Remove o item de índice 1 e armazena na variável
fruta_removida = frutas.pop() # Se não indicar um índice, remove o último elemento

print(fruta_removida)
print(frutas)

# Removendo pelo índice e retorna a lista sem o elemento removido (del [])

frutas = ["maçã", "banana", "laranja"]

del frutas[0]

print(frutas)

# Tamanho da lista len()

frutas = ["maçã", "banana", "laranja"]

print(len(frutas))

# Percorrendo uma lista

nomes = ["ana", "Carlos", "marina"]

for nome in nomes:
    print(nome)