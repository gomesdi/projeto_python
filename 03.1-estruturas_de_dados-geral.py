# Comparação geral

# Estrutura	    Ordenada	        Mutável	    Permite duplicados	Acesso
# Lista	        Sim	                   Sim	     Sim	            Por índice
# Tupla	        Sim	                   Não	     Sim	            Por índice
# Dicionário    Sim, pela inserção	   Sim	     Chaves únicas	    Por chave
# Set	        Não possui índice	   Sim	     Não	            Por valor

# Escolhendo a estrutura correta
# Use:

# Lista quando tiver uma sequência de valores que pode ser alterada;
# Tupla quando tiver uma sequência fixa que não deve ser modificada;
# Dicionário quando precisar relacionar chaves e valores;
# Set quando precisar evitar duplicados ou comparar conjuntos.
# Exemplo prático:


aluno = {
    "nome": "Diego",
    "notas": [8.5, 7.0, 9.0],
    "disciplinas": ("Python", "Django"),
    "habilidades": {"Python", "Git", "SQL"},
}
# Nesse exemplo:

# aluno é um dicionário;
# "notas" contém uma lista;
# "disciplinas" contém uma tupla;
# "habilidades" contém um set.
# Estruturas de dados podem ser combinadas umas dentro das outras.