class Situacao:
    def calcular_desconto_extra(self):
        return 0

    def aprovar(self):
        raise Exception("Não é possível aprovar o orçamento!")

    def reprovar(self):
        raise Exception("Não é possível reprovar o orçamento!")

    def finalizar(self):
        raise Exception("Não é possível finalizar o orçamento!")
