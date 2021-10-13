from src.orcamento.orcamento import Orcamento


class Desconto:
    def __init__(self, proximo):
        self.proximo = proximo

    def calcular(self, orcamento: Orcamento):
        if self.deve_aplicar(orcamento):
            return self.aplica(orcamento)
        return self.proximo.calcular(orcamento)

    def aplica(self, orcamento: Orcamento):
        raise NotImplementedError

    def deve_aplicar(self, orcamento: Orcamento):
        raise NotImplementedError
