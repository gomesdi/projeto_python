#Exercício 1
nome = input("Digite sue nome: ")
idade = int(input("Digite sua idade: "))
cidade = input("Digite a cidade que você mora: ")

print(f"Meu nome é {nome}, eu tenho {idade} anos e moro em {cidade}")

#Exercício 2
num1 = 100
num2 = 50

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2

print(f"O valor da soma entre {num1} e {num2} é: {soma}")
print(f"O valor da subtração entre {num1} e {num2} é: {subtracao}")
print(f"O valor da multiplicação entre {num1} e {num2} é: {multiplicacao}")
print(f"O valor da divisão entre {num1} e {num2} é: {divisao}")

#Exercício 3
num_a = int(input("Informe o primeiro número: "))
num_b = int(input("Informe o segundo número: "))

print(f"A soma dos números é: {num_a + num_b}")
print(f"O resto da divisão dos números é: {num_a % num_b}")
print(f"O primeiro número elevado ao segundo é: {num_a ** num_b}")

#Exercício 4
nome_produto = input("Informe o nome do produto: ")
preco_produto = float(input("Informe o praço do produto (R$): "))
quantidade_produto = int(input("Informe a quantidade de produtos: "))

valor_total = preco_produto * quantidade_produto

print(f"O valor total da compra do {nome_produto} será de {valor_total}")