import datetime

class Historico:
    def __init__(self):
        self.__transacoes = []
    
    @property
    def transacoes(self):
        return self.__transacoes
    
    def adicionar_transacao(self, tipo, valor):
        self.__transacoes.append({
            "tipo": tipo,
            "valor": valor,
            "data": datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        })
