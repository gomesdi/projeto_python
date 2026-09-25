# DICIONÁRIOS

# Armazena dados no formato chave: valor

pessoa = {
    "nome": "Diego",
    "idade": 42,
    "cidade": "Fortaleza",
}

print(pessoa)
print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["cidade"])

# .get() => forma de acessar o elemento

print(pessoa.get("nome"))


# este método não gera erro caso a chave não exista
print(pessoa.get("profissão"))
print(pessoa.get("profissão", "Não informado"))

# Alterando valores

pessoa["idade"] = 43

print(pessoa)

# Verificando se a chave existe

if "nome" in pessoa:
    print("A chave nome existe em pessoas")
    

# Percorrendo um dicionário

# Chaves
for chave in pessoa:
    print(chave)
    
# Valores
for valor in pessoa.values():
    print(valor)
    
# chaves e valores

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

