from src.desconto.desconto import Desconto
from src.orcamento.orcamento import Orcamento


class DescontoValorMaiorQueQuinhentos(Desconto):
    def __init__(self, proximo):
        super().__init__(proximo)

    def calcular(self, orcamento: Orcamento):
        if orcamento.get_valor() > 500:
            return orcamento.get_valor()*0.05
        return self.proximo.calcular(orcamento)
