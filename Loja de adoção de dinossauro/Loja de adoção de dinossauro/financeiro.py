class Financeiro:
    def __init__(self):
        self.saldo = 0
        self.historico = []

    def registrar_receita(self, valor, descricao=""):
        self.saldo += valor
        self.historico.append(("Receita", valor, descricao))
        print(f"Receita registrada: +R${valor} ({descricao})")

    def registrar_despesa(self, valor, descricao=""):
        self.saldo -= valor
        self.historico.append(("Despesa", valor, descricao))
        print(f"Despesa registrada: -R${valor} ({descricao})")

    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo}")
        return self.saldo

    def consultar_historico(self):
        if not self.historico:
            print("Nenhuma movimentação registrada.")
        else:
            print("\n Histórico Financeiro:")
            for tipo, valor, descricao in self.historico:
                print(f"- {tipo}: R${valor} | {descricao}")
