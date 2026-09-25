class Veiculo:
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def ligar(self):
        return f"O Veículo {self.marca} {self.modelo} esta ligado!"


carro1 = Veiculo("Honda", "Civic")
carro2 = Veiculo("Fiat", "Toro")
carro3 = Veiculo("Toyota", "corolla")


class Carro(Veiculo):
    def __init__(self, marca, modelo, numero_portas):
        super().__init__(marca, modelo)
        self.numero_portas = numero_portas
        
    def ligar(self):
        # Opcional: você pode usar o super().ligar() aqui se quiser aproveitar o texto original
        return "Carro ligado"

class Moto(Veiculo):
    def __init__(self, marca, modelo, tem_carenagem):
        super().__init__(marca, modelo)
        self.tem_carenagem = tem_carenagem
        
    def ligar(self):
        return "Moto ligada"

# Testando os novos objetos
carro1 = Carro("VW", "Polo", "4 portas")
moto1 = Moto("Honda", "CB 500", tem_carenagem=True)

print(carro1.ligar())
print(moto1.ligar())