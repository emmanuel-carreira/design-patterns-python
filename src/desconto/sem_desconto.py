from src.desconto.desconto import Desconto
from src.orcamento.orcamento import Orcamento


class SemDesconto(Desconto):
    def __init__(self):
        super().__init__(None)

    def calcular(self, orcamento: Orcamento):
        return 0
