# 1.Conceito básicos

# Conceito	                                O que é	                                                Como se declara em Python
# Classe	                    Modelo que define atributos e métodos	                               class NomeDaClasse:
# Instância	                Objeto concreto criado a partir da classe	                               obj = NomeDaClasse()
# Atributo	                Variável associada à classe ou à instância	           self.nome = valor (instância) ou NomeDaClasse.atributo (classe)
# Método	                    Função que opera sobre a instância (ou classe)	                       def metodo(self, ...):
# Herança	                    Reuso de código: classe filha herda de classe pai	                    class Filho(Pai):
# Construtor (__init__)	    Executado ao criar a instância; inicializa atributos	                   def __init__(self, ...):


# 2. Estrutura de uma classe simples

class Pessoa:
    # Atributo de classe (compartilhado por todas as instâncias)
    especie = "Humano"

    def __init__(self, nome, idade):
        # Atributos de instância
        self.nome = nome
        self.idade = idade

    # Método de instância
    def apresentar(self):
        return f"Olá, eu sou {self.nome} e tenho {self.idade} anos."

    # Método de classe
    @classmethod
    def tipo_especie(cls):
        return f"Todos somos da espécie {cls.especie}"

    # Método estático (não depende de classe nem instância)
    @staticmethod
    def saudacao():
        return "Bem‑vindo ao mundo da POO!"
    
# Cria duas instâncias
p1 = Pessoa("Ana", 30)
p2 = Pessoa("Bruno", 25)

print(p1.apresentar())          # → Olá, eu sou Ana e tenho 30 anos.
print(p2.apresentar())          # → Olá, eu sou Bruno e tem 25 anos.
print(Pessoa.tipo_especie())    # → Todos somos da espécie Humano
print(Pessoa.saudacao())        # → Bem‑vindo ao mundo da POO!


# 3. Herança e sobrescrita de métodos

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        # Chama o construtor da classe pai
        super().__init__(nome, idade)
        self.cargo = cargo

    # Sobrescreve o método apresentar
    def apresentar(self):
        base = super().apresentar()
        return f"{base} Eu trabalho como {self.cargo}."
# Uso:
    
f = Funcionario("Carla", 28, "Desenvolvedora")
print(f.apresentar())
# → Olá, eu sou Carla e tenho 28 anos. Eu trabalho como Desenvolvedora.



# 4. Encapsulamento (atributos “privados”)

# Em Python, o prefixo __ (duplo underline) nomeia mangling, dificultando o acesso externo.
# Não há privacidade real, mas é uma convenção.

class ContaBancaria:
    def __init__(self, saldo=0):
        self.__saldo = saldo   # “privado”

    def depositar(self, valor):
        if valor < 0:
            raise ValueError("Valor inválido")
        self.__saldo += valor

    def sacar(self, valor):
        if valor > self.__saldo:
            raise ValueError("Saldo insuficiente")
        self.__saldo -= valor

    def extrato(self):
        return self.__saldo



# 5. Polimorfismo (mesmo método, comportamentos diferentes)

class Animal:
    def falar(self):
        raise NotImplementedError

class Cachorro(Animal):
    def falar(self):
        return "Au Au!"

class Gato(Animal):
    def falar(self):
        return "Miau!"

animais = [Cachorro(), Gato()]
for a in animais:
    print(a.falar())
# Saída:
# Au Au!
# Miau!

