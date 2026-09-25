# # FUNÇÕES

# def saudacao1():
#     print("Olá, Diego!")

# saudacao1()

# # Função com parâmetro
# def saudacao2(nome):
#     print(f"Olá, {nome}")

# saudacao2("Diego")
# saudacao2("Andressa")

# # Função com parâmetro externo
# nome = input("Diegite seu nome: ")
# saudacao2(nome)

# # Função com multiplos parâmetros

# def apresentacao(nome, idade):
#     print(f"Meu nome é {nome} e eu tenho {idade} anos.")

# apresentacao("Diego", 41)

# Função com retorno

# def somar(a, b):
#     return a + b

# print(somar(10, 25))

# # Guardando a função em uma variável
# resultado_soma = somar(10, 5)
# print(resultado_soma)

# Print vs Return

# Em funções com print a função apenas exibe o resultado,
# mas não se consegue retornar o resultado
# isso impede que se armazene o seu conteúdo em uma variável.

# Regra prática
# Use print quando quiser apenas mostrar algo na tela.
# Use return quando quiser devolver um valor para ser reutilizado.

# Exemplo: Nesse caso o return permite que a função seja armazenada em uma variável
#          e reaproveitada em outro momento no código.

# def calcular_media(nota_01, nota_02):
#     return (nota_01 + nota_02)/2

# media = calcular_media(10, 8)

# if media > 7:
#     print("Aprovado")
# else:
#     print("Reprovado")


# # Função com multiplos retornos

# def calcular(a, b):
#     soma = a + b
#     multiplicacao = a * b

#     return soma, multiplicacao

# valores = calcular(10, 15)
# print(valores)

# valor_soma, valor_multiplicacao = calcular(4, 3)

# print(f"O valor da soma é {valor_soma}.")
# print(f"O valor da multiplicação é {valor_multiplicacao}.")

# # Retorno antecipado
# # Sempre que a função encontra "return" ela será encerrada

# def verificar_idade(idade):
#     if idade < 0:
#         return "Idade inválida"

#     if idade >= 18:
#         return "Maior de idade"

#     return "Menor de idade"

# print(verificar_idade(25))
# print(verificar_idade(15))
# print(verificar_idade(-10))

# # parâmetros com valor padrão:
# OBS: Parâmetros com valor padrão devem aparecer sempre
# depois de parâmetros sem valor padrão

# def saudacao(nome, mensagem = "Olá"):
#     print(f"{mensagem}, {nome}")

# saudacao("Diego")
# saudacao("Diego", "Bom dia")

# def calcular_desconto(valor, desconto = 10):
#     return valor - (valor * (desconto/100))

# print(calcular_desconto(100))
# print(calcular_desconto(100, 20))

# # Argumentos nomeados

# def apresentar(
#     nome="Diego",
#     idade="30",
#     cidade="São Paulo"
# ):
#     print(f"{nome} tem {idade} anos e mora em {cidade}.")

# apresentar()

# # *args: quantidade variável de argumentos posicionais
# # O *args permite que a função receba vários argumentos posicionais.

# def somar_varios(*numeros):
#     total = 0

#     for numero in numeros:
#         total += numero

#     return total

# print(somar_varios(1,2,3,4,5,6,7,8,9,10))
# print(somar_varios(1,3,5,7,9))
# print(somar_varios(2,4,6,8,10))
# print(type(somar_varios()))

# def mostrar_args(*args):
#     print(args)
#     print(type(args))

# mostrar_args("Python", 3.12, True)

# def exibir_mensagens(prefixo, *mensagens):
#     for mensagem in mensagens:
#         print(f"{prefixo}: {mensagem}")

# exibir_mensagens("INFO", "Sistema iniciado", "Usuário conectado")

# # **kwargs: quantidade variável de argumentos nomeados

# def exibir_dados(**dados):
#     print(dados)

# exibir_dados(nome="Diego", idade=30, cidade="Fortaleza")

# def exibir_dados(**dados):
#     for chave, valor in dados.items():
#         print(f"{chave}: {valor}")

# exibir_dados(
#     nome="Diego",
#     linguagem="Python",
#     nivel="Iniciante"
# )

# # *args e **kwargs

# def mostrar_informacoes(*args, **kwargs):
#     print("Argumentos posicionados: ", args)
#     print("Argumentos nomeados: ", kwargs)

# mostrar_informacoes(
#     "Python",
#     "Django",
#     nome="Diego",
#     idade=42,
# )

# Desempacotamento de argumentos
# Listas

# def exibir(a, b, c):
#     return a, b, c

# valores = [10, 20, 30]

# print(exibir(*valores))


# def soma(n1, n2, n3):
#     return n1 + n2 + n3

# numeros = [50, 120, 15]

# print(soma(*numeros))

# Dicionário

# def apresentar(nome, idade, cidade):
#     print(f"{nome} tem {idade} anos e mora em {cidade}.")

# dados = {
#     "nome": "Diego",
#     "idade": 40,
#     "cidade": "Fortaleza"
# }

# apresentar(**dados)

# Funções com valores

# def dizer_oi():
#     print("oi!")


# funcao = dizer_oi

# funcao()


# def dizer_oi():
#     return "oi!"


# funcao = dizer_oi

# print(funcao)


# def executar(funcao):
#     funcao()


# def mensagem():
#     print("Executando função...")


# executar(mensagem)


# Documentação com docstrings
# Uma docstring explica o que uma função faz:


# def calcular_area_retangulo(largura, altura):
#     """
#     Calcula a área de um retângulo.

#     Parâmetros:
#         largura: largura do retângulo.
#         altura: altura do retângulo.

#     Retorna:
#         A área do retângulo.
#     """
#     return largura * altura

# print(f"A área do retangulo é: {calcular_area_retangulo(10,5)}")

# Podemos consultar a documentação:
# help(calcular_area_retangulo)

## Exemplo completo

def calcular_media(notas):
    if not notas:
        return 0
    
    return sum(notas) / len(notas)

def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    
    elif media >= 5:
        return "Recuperaçao"
    
    else:
        return "Reprovado"

def exibir_resultado(nome, notas):
    media = calcular_media(notas)
    situacao = verificar_situacao(media)

    print(f"Aluno: {nome}")
    print(f"Notas: {notas}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")

exibir_resultado("Diego", [8, 7, 9])