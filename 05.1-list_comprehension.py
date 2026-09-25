# # LIST COMPREHENTION

# # Método tradicional
# quadrados = []

# for numero in range (1,6):
#     quadrados.append(numero**2)
    
# print(quadrados)

# # List comprehentsion

# quadrados = [numero ** 2 for numero in range(2,11,2)]

# print(quadrados)

# # Estrutura básica
# # [expressao for item in iteravel]

# # expressão: numero ** 2
# # item: numero
# # objeto percorrido: range (2,11,2)

# nomes = ["ana", "maria", "carlos"]

# nomes_maiusculos = [nome.upper() for nome in nomes]

# print(nomes_maiusculos)

# # LC com condição
# #1
# numeros = [1,2,3,4,5,6,7,8,9,10]

# pares = [numero for numero in numeros if numero % 2 == 0]

# print(pares)

# #2
# palavras = ["python", "java", "c", "javascript"]

# palavras_longas = [
#     palavra for palavra in palavras
#     if len(palavra) > 3
# ]

# print(palavras_longas)

# #List comprehension com if e else
# # Quando usamos else, a condição fica antes do for:

# # A estrutura é:

# # [valor_se_verdadeiro if condicao else valor_se_falso for item in iteravel]

# numeros = [1,2,3,4,5,6]

# resultado = [
#     "par" if numero % 2 == 0 else "ímpar"
#     for numero in numeros
# ]

# print(resultado)

# # List comprehension com strings

# palavra = "python"

# letras = [letra.upper() for letra in palavra]

# print(letras)

# palavra = "programacao"

# vogais = [
#     letra for letra in palavra
#     if letra in "aeiou"
# ]

# print(vogais)

# #List comprehension com listas aninhadas
# matriz = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# elementos = [
#     numero
#     for linha in matriz
#     for numero in linha
# ]

# print(elementos)