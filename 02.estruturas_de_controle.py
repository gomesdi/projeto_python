# nomes = ["Ana", "Bia", "Cris"]

# for nome in nomes:
#     print(nome)

# palavra = "Python"

# for letra in palavra:
#     print(letra)

# for numero in range(1, 6):
#     print(numero)

# print("----------------------------")


# for numero in range(0, 11, 2):
#     print(numero)

# print("----------------------------")

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for numero in numeros:
#     if numero % 2 == 0:
#         print(numero)


# idade = 1

# while idade <= 10:
#     print(idade)
#     idade += 1

# senha = ""

# while senha != "123":
#     senha = input("Digite a senha: ")

# print("Acesso permitido")
# print("FIM!")


# while True:
#     comando = input("Digite 'sair' para encerrar: ")

#     if comando == "sair":
#         break

#     print(f"Você digitou {comando}")
# print("Programa encerrado")


# for numero in range (1, 10):
#     if numero % 2 == 0:
#         continue

#     print(numero)


# while True:
#     numero = int(input("Digite um numero, ou 0 para sair: "))

#     if numero == 0:
#         break

#     if numero >0:
#         print(f"O numero {numero} é positivo")
#     else:
#         print(f"O numero {numero} é negativo")

# print(f"Programa Encerrado!")

# #Exercício 1:
# user_age = int(input("Insert your age: "))

# if user_age >= 18:
#     print(f"Você é maior de idade!")
# else:
#     print(f"Voçê é menor de idade!")

# #Exercício 2:
# note = float(input("Digite sua nota: "))

# if note >= 7:
#     print(f"Aprovado!")
# elif 5 <= note <= 6.9:
#     print(f"Recuperação")
# else:
#     print(f"Reprovado")

# #Exercício 3
# for numeros in range(1, 21):
#     print(numeros)

# #Exercício 4
# for numeros in range(1, 31):
#     if numeros % 2 ==0:
#         print(numeros)

# #Exercício 5
# numero = 10

# while numero >= 0:
#     print(numero)
#     numero -= 1


# #Exercício 6
# senha = ""

# while True:

#     senha = input("Digite sua senha: ")
#     if senha == "python123":
#         break

# print("Acesso permitido")

# Desafio
saldo = 1000
saque = 0
deposito = 0

while True:
    print("\n     MENU")
    print("---------------")
    print("\n1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("0 - Sair")

    opcao = int(input("\nDigite sua opção: "))

    if opcao == 1:
        print(f"\nSeu saldo atual é de R${saldo:.2f}")

    elif opcao == 2:
        deposito = float(input("Informe o valor a ser depositado: "))
        saldo += deposito
        print(f"\nFoi depositado R${deposito:.2f} na sua conta")
        print(f"Seu saldo atual é de R${saldo:.2f}")

    elif opcao == 3:
        saque = float(input("Informe o valor a ser sacado: "))
        
        if saque > saldo:
            print("ATENÇÃO!!!")
            print("Saldo insuficiente para este valor")
        else:
            saldo -= saque
            print(f"\nFoi retirado R${saque:.2f} na sua conta")
            print(f"Seu saldo atual é de R${saldo:.2f}")

    elif opcao == 0:
        print("Você saiu da aplicação")
        break

    else:
        print("Opção inválida")

