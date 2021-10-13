from src.desconto.desconto import Desconto
from src.orcamento.orcamento import Orcamento


class DescontoMaisQueCincoItens(Desconto):
    def __init__(self, proximo):
        super().__init__(proximo)

    def calcular(self, orcamento: Orcamento):
        if orcamento.get_quantidade_itens() > 5:
            return orcamento.get_valor()*0.1
        return self.proximo.calcular(orcamento)
