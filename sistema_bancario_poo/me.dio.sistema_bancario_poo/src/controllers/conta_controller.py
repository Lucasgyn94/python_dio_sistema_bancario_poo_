from models.conta import Conta

class ContaController:
    def __init__(self):
        self.numero_conta = 0

    def criar_conta(self, cliente, valor_deposito):
        self.numero_conta += 1
        numero_conta = str(self.numero_conta).zfill(4)  
        agencia = "2408" 
        conta = Conta(cliente, numero_conta, agencia)
        conta.depositar(valor_deposito)
        cliente.adicionar_conta(conta)
        return conta

    def buscar_conta_por_numero(self, cliente, numero):
        for conta in cliente.contas:
            if conta.numero_conta == numero:
                return conta
        return None

    def realizar_deposito(self, conta, valor):
        return conta.depositar(valor)

    def realizar_saque(self, conta, valor):
        return conta.sacar(valor)

    def ver_saldo(self, conta):
        return conta.saldo
    
    def ver_extrato(self, conta):
        return conta.historico.transacoes
