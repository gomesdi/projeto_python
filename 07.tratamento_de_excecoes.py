# def sacar(saldo, valor):
#     if valor > saldo:
#         raise ValueError("Saldo insuficiente para saque.")
#     return saldo - valor

# try:
#     sacar(100, 150)
# except ValueError as e:
#     print(e)

# try:
#     sacar(100, 150)
# except ValueError as e:
#     print("Log: erro ao sacar")
#     raise  # relança a mesma exceção para quem chamou

class SaldoInsuficienteError(Exception):
    """Levantada quando o saque excede o saldo disponível."""
    pass


class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError(
                f"Saldo de {self.saldo} insuficiente para sacar {valor}."
            )
        self.saldo -= valor
        return self.saldo


conta = ContaBancaria(100)

try:
    conta.sacar(150)
except SaldoInsuficienteError as e:
    print(f"Operação negada: {e}")