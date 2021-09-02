from src.imposto.imposto import Imposto
from src.orcamento.orcamento import Orcamento


class Iss(Imposto):
    def calcular(self, orcamento: Orcamento):
        return orcamento.get_valor() * 0.06
