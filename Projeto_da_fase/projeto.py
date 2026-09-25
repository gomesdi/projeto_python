import json
import os

ARQUIVOS_CONTATOS = "contatos.json"


def carregar_contatos():
    if not os.path.exists(ARQUIVOS_CONTATOS):
        return[]
    
    try:
        with open(ARQUIVOS_CONTATOS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (json.JSONDecodeError, IOError):
        print("Aviso: não foi possível ler o arquivo. Iniciando lista vazia.")
        return []

def salvar_contato(contatos):
    with open(ARQUIVOS_CONTATOS, "w", encoding="utf-8") as arquivo:
        json.dump(contatos, arquivo, indent=4, ensure_ascii=False)


def adicionar_contato(contatos):
    nome = input("Nome:").strip()
    telefone = input("Telefone: ").strip()
    email = input("Email: ").strip() 
    
    contato = {
        "nome": nome,
        "telefone": telefone, 
        "email": email,
    }
    
    contatos.append(contato)
    salvar_contato(contatos)
    
    print(f"Contato {nome} adicionado com sucesso!")


def listar_contatos(contatos):
    if not contatos:
        print("Nenhum contato encontrado.")
        return
    
    print("\n===== Lista de Contatos =====")
    for i, contato in enumerate(contatos, start=1):
        print(f"\n Contato{i}")
        print(f"Nome: {contato['nome']}")
        print(f"Telefone: {contato['telefone']}")
        print(f"Email: {contato['email']}")


def buscar_contato(contatos):
    termo_de_busca = input("Digite o nome do contato que deseja buscar: ").strip().lower()
    
    if not termo_de_busca:
        print("O campo para busca não pode estar vazio.")
        return
    
    resultados = [
        contato 
        for contato in contatos 
        if termo_de_busca in contato['nome'].lower()
    ]
    
    termo_de_busca = termo_de_busca.title()
    
    if not resultados:
        print(f"Nenhum contato encontrado com o nome: {termo_de_busca}")
        return
    
    print(f"\n===== Resultados da Busca para '{termo_de_busca}' =====")
    
    for i, contato in enumerate(resultados, start=1):
        print(f"\nContato {i}")
        print(f"Nome: {contato['nome']}")
        print(f"Telefone: {contato['telefone']}")
        print(f"Email: {contato['email']}")


def remover_contato(contatos):
    if not contatos:
        print("Nenhum contato cadastrado.")
        return
    
    print("\n==== Contatos Cadastrados ====")
    
    for i, contato in enumerate(contatos, start=1):
        print(f"{i}. {contato['nome']} - {contato['telefone']} - {contato['email']}")
    
    try:
        numero = int(input("Digite o número do contato que deseja remover: "))
    except ValueError:
        print("Opção inválida. Por favor, digite um número de contato válido.")
        return
    
    if numero < 1 or numero > len(contatos):
        print("Número de contato inválido.")
        return

    contato_removido = contatos.pop(numero - 1)
    salvar_contato(contatos)
    
    print(f"Contato {contato_removido['nome']} removido com sucesso!")


def exibir_menu():
    print("\n===== Gerenciador de Contatos =====")
    print("1. Adicionar Contato")
    print("2. Listar Contatos")
    print("3. Buscar Contato")
    print("4. Remover Contato")
    print("0. Sair")


def main():
    contatos = carregar_contatos()
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            adicionar_contato(contatos)
        elif opcao == "2":
            listar_contatos(contatos)
        elif opcao == "3":
            buscar_contato(contatos)
        elif opcao == "4":
            remover_contato(contatos)
        elif opcao == "0":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()