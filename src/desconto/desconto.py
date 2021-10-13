from src.orcamento.orcamento import Orcamento


class Desconto:
    def __init__(self, proximo):
        self.proximo = proximo

    def calcular(self, orcamento: Orcamento):
        raise NotImplementedError
