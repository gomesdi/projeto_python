# arquivo = open("08.mensagem.txt", "r")
# conteudo = arquivo.read()
# arquivo.close()
# print(conteudo)


# with open("08.mensagem.txt", "w", encoding="utf-8") as arquivo:
#     conteudo = arquivo.write("Olá, estou estudando python!")
# print(conteudo)


# with open("08.mensagem.txt", "r", encoding="utf-8") as arquivo:
#     conteudo = arquivo.read()
# print(conteudo)


# with open ("08.mensagem.txt", "r", encoding="utf-8") as arquivo:
#     for linha in arquivo:
#         print(linha.strip())

# with open("08.mensagem.txt", "r", encoding="utf-8") as arquivo:
#     linhas = arquivo.readlines()

# print(linhas)

# with open("08.anotacoes.txt", "w", encoding="utf-8") as arquivo:
#     arquivo.write("Primeira anotação.")

# with open ("08.texto.txt", "w", encoding="utf-8") as arquivo:
#     arquivo.write("primeira linha\n")
#     arquivo.write("segunda linha\n")
#     arquivo.write("terceira linha\n")

# with open ("08.texto.txt", "r", encoding="utf-8") as arquivo:
#     for linha in arquivo:
#         print(linha.strip())


# linhas = [
#     "Primeiro Colocado\n"
#     "Segundo Colocado\n"
#     "Terceiro Colocado\n"
# ]

# with open("08.colocacao.txt", "w", encoding="utf-8") as arquivo:
#     arquivo.writelines(linhas)

# print(linhas)

# with open("08.colocacao.txt", "a", encoding="utf-8") as arquivo:
#     arquivo.write("Quarto colocado\n")
#     arquivo.write("Quinto colocado\n")
#     arquivo.write("Sexto colocado\n")

# try:
#     with open("arquivo_inexistente.txt", "r", encoding="utf-8") as arquivo:
#         conteudo = arquivo.read()

#     print(conteudo)

# except FileNotFoundError:
#     print("O arquivo não foi encontrado.")


# try:
#     with open("dados.txt", "r", encoding="utf-8") as arquivo:
#         conteudo = arquivo.read()

# except FileNotFoundError:
#     print("Arquivo não encontrado.")

# except PermissionError:
#     print("Você não tem permissão para acessar esse arquivo.")





# import os

# if os.path.exists("08.texto.txt"):
#     print("O arquivo existe.")
# else:
#     print("O arquivo não existe.")





# from pathlib import Path

# caminho = Path("dados.txt")

# if caminho.exists():
#     print("O arquivo existe.")
# else:
#     print("O arquivo não existe.")




# from pathlib import Path

# caminho = Path("08.mensagens.txt")

# caminho.write_text("Olá, Python!", encoding="utf-8")

# conteudo = caminho.read_text(encoding="utf-8")

# print(conteudo)




# from pathlib import Path

# pasta = Path("08.dados")
# pasta.mkdir(exist_ok=True)

# arquivo = pasta / "clientes.txt"

# arquivo.write_text("Ana\nBruno\nCarlos", encoding="utf-8")




# def adicionar_tarefa(tarefa):
#     with open("08.tarefas.txt", "a", encoding="utf-8") as arquivo:
#         arquivo.write(f"{tarefa}\n")


# def listar_tarefas():
#     try:
#         with open("08.tarefas.txt", "r", encoding="utf-8") as arquivo:
#             tarefas = arquivo.readlines()

#         for indice, tarefa in enumerate(tarefas, start=1):
#             print(f"{indice}. {tarefa.strip()}")

#     except FileNotFoundError:
#         print("Nenhuma tarefa cadastrada.")


# adicionar_tarefa("Estudar arquivos em Python")
# adicionar_tarefa("Praticar o uso de with")

# listar_tarefas()
