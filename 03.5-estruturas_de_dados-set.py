# SET

# Sets são:

# Não indexados;
# Mutáveis;
# Não permitem valores repetidos;
# Úteis para eliminar duplicidades e fazer operações matemáticas de conjuntos.

numeros = {1, 2, 3, 3, 2, }

print(numeros)

# Adicionando elementos .add():  Adiciona no primeiro elemento

frutas = {"laranja", "maçã"}

frutas.add("banana")
print(frutas)

# Removendo elementos .remove() or .discard()

frutas.remove("banana")
print(frutas)

fruta = {"laranja", "maçã"}
fruta.discard("laranja")
# Discard não vai gerar erro se o elemento não existir
fruta.discard("uva")
print(fruta)


# Verificando existencia de elemento:

frutas = {"maçã", "banana", "laranja"}

if "banana" in frutas:
    print("Banana encontrada")
    
# Operação entre sets

numeros_a = {1, 2, 3, 4}
numeros_b = {3, 4, 5, 6}

# União: 
# Junta todos os elementos:

print(numeros_a | numeros_b)

print(numeros_a.union(numeros_b))

# interseção: 
# Retorna apenas os elementos presentes nos dois conjuntos:


print(numeros_a & numeros_b)

# Diferença: 
# Retorna os elementos que estão no primeiro conjunto, mas não no segundo

print(numeros_a - numeros_b)

