# TUPLAS

# Uma tupla é parecida com uma lista, mas não pode ser alterada depois de criada.

# As tuplas são:
#   - Ordenadas;
#   - Imutáveis;
#   - Permitem valores repetidos;
#   - Acessadas por índices.

cores = ("vermelho", "verde", "azul")

print(cores[0])

# cores[0] = "amarelo" => ERRO: Os elementos de tupla não podem ser alterados!

dias_da_semana = (
    "segunda", 
    "terça",
    "quarta",
    "quinta",
    "sexta",
    "sábado",
    "domingo",
)

meses = (
    "janeiro", 
    "fevereiro", 
    "março"
)

# Tupla com um elemento
# Para criar uma tupla com apenas um elemento, é necessário usar uma vírgula:
# Criar sem a vírgula, fica apenas um número entre parêntesses.

valor = (10,)
valor2 = (10)

print(type(valor))
print(type(valor2))