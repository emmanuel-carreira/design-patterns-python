from src.desconto.desconto import Desconto
from src.orcamento.orcamento import Orcamento


class DescontoMaisQueCincoItens(Desconto):
    def __init__(self, proximo):
        super().__init__(proximo)

    def aplica(self, orcamento: Orcamento):
        return orcamento.valor*0.1

    def deve_aplicar(self, orcamento: Orcamento):
        return orcamento.quantidade_itens > 5
