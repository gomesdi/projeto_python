def somar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

PI = 3.14159

if __name__ == "__main__":
    print(multiplicar(4, 8))

# Isso permite criar código que só roda quando o arquivo é
# executado diretamente, mas não quando é importado:

# Quando você executa o arquivo diretamente (python matematica.py), __name__ vale "__main__".
# Quando você importa o arquivo em outro lugar, __name__ vale o nome do módulo ("matematica").

# Isso é usado para colocar testes rápidos ou um "modo de execução" dentro do próprio módulo sem que isso interfira quando o módulo for importado como biblioteca.

# Pacotes: organizando módulos em pastas
# Um pacote é simplesmente uma pasta que contém módulos, e que o Python reconhece como um "pacote importável" graças a um arquivo especial: __init__.py.

# Estrutura de exemplo:

# meu_projeto/
# ├── main.py
# └── operacoes/
#     ├── __init__.py
#     ├── basicas.py
#     └── avancadas.py


# # operacoes/basicas.py
# def somar(a, b):
#     return a + b

# # operacoes/avancadas.py
# def potencia(base, expoente):
#     return base ** expoente


# from operacoes.basicas import somar
# from operacoes.avancadas import potencia
# from operacoes import basicas  # importa o módulo inteiro

# print(somar(2, 3))
# print(potencia(2, 10))

# O que faz o __init__.py?
# Ele indica ao Python que aquela pasta deve ser tratada como um pacote.
# Pode ficar vazio (é o mais comum e suficiente na maioria dos casos).
# Pode conter código que roda quando o pacote é importado, ou controlar o que fica disponível ao fazer from pacote import * usando a variável __all__.

# Em versões modernas do Python (3.3+), tecnicamente é possível criar "namespace packages" sem __init__.py, mas para aprendizado, sempre use __init__.py — é mais explícito e é o padrão que você vai encontrar em 99% dos projetos reais, incluindo Django.

# Imports absolutos vs relativos
# Absoluto (recomendado): caminho completo a partir da raiz do projeto.
#   from operacoes.basicas import somar
# Relativo (usado dentro de pacotes, entre módulos irmãos):
#   from .basicas import somar      # mesmo nível
#   from ..outro_pacote import algo # nível acima