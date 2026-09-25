# 1. Criar pasta do projeto e entrar nela
# mkdir meu_projeto
# cd meu_projeto

# # 2. Criar ambiente virtual
# python -m venv venv

# # 3. Ativar
# source venv/bin/activate   # ou venv\Scripts\activate no Windows

# # 4. Instalar dependências
# pip install django
# pip install requests==2.31.0

# # 5. Congelar dependências
# pip freeze > requirements.txt

# # 6. Trabalhar normalmente...

# # 7. Ao terminar a sessão
# deactivate

# Boas práticas
# Nunca suba a pasta venv/ para o Git — ela é grande e específica da sua máquina. Adicione ao .gitignore:
#   venv/
# Sempre gere/atualize o requirements.txt antes de compartilhar ou fazer commit importante.
# Um ambiente virtual por projeto, nunca compartilhe entre projetos diferentes.
# Ao clonar um projeto de outra pessoa, o fluxo é: criar venv → ativar → pip install -r requirements.txt.

# Exercício prático
# Crie uma pasta chamada teste_venv.
# Dentro dela, crie um ambiente virtual chamado venv.
# Ative o ambiente.
# Instale o pacote requests.
# Gere o requirements.txt.
# Desative o ambiente, apague a pasta venv/ e recrie tudo usando apenas o requirements.txt para reinstalar as dependências.
# Isso simula exatamente o que acontece quando você (ou outra pessoa) baixa um projeto do zero.


# zsh# 1. Remova a pasta venv antiga (garanta que está na pasta certa antes)
# rm -rf venv

# # 2. Crie o novo ambiente virtual usando python3
# python3 -m venv venv

# # 3. Ative o novo ambiente virtual
# source venv/bin/activate

# # 4. Atualize o gerenciador de pacotes (boa prática)
# pip install --upgrade pip

# # 5. Instale todas as dependências do arquivo
# pip install -r requirements.txt

# # 6. Verifique se deu certo
# pip list