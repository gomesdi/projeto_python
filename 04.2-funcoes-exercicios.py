## FUNÇÔES EXERCÌCIOS

## Exercício 1 — Saudação
## Crie uma função chamada saudacao que receba um nome e retorne:

## Olá, [nome]!


# def saudacao(nome):
#     return f"Olá, {nome}"

# print(saudacao("Diego"))

# Exercício 2 — Par ou ímpar
# Crie uma função chamada eh_par que receba um número e retorne True se ele for par e False caso contrário.

# def eh_par(numero):
#     if numero % 2 == 0:
#         return True
#     else:
#         return False

# print(eh_par(10))
# print(eh_par(7))

# # Exercício 3 — Maior número
# # Crie uma função chamada maior_numero que receba vários números usando *args e retorne o maior deles.

# def maior_numero(*args):
#     if not args:
#         return None
#     return max(args)

# print(maior_numero(4, 9, 2, 15, 7))

# Exercício 4 — Cadastro
# Crie uma função chamada criar_usuario que receba:

# nome;
# idade;
# outras informações usando **kwargs.
# A função deve retornar um dicionário com todos os dados.


# def criar_usuario(nome, idade, **kwargs):
#     return {
#         "nome": nome,
#         "idade": idade,
#         **kwargs,
#     }

# usuario = criar_usuario(
#     "Diego",
#     30, 
#     cidade="São Paulo",
#     linguagem="Python"
# )

# print(usuario)

# Exercício 5 — Conversor de temperatura
# Crie duas funções:

# celsius_para_fahrenheit(celsius);
# fahrenheit_para_celsius(fahrenheit).
# As fórmulas são:

# F=C*(9/5)+32
# C=(F-32)*(5/9)

def celcius_para_fahrenheit(c):
    f=0
    f = c *(9/5)+32
    return f


def fahrenheit_para_celcius(f):
    c = 0
    c = (f-32)*(5/9)
    return c

print(celcius_para_fahrenheit(0))
print(fahrenheit_para_celcius(212))