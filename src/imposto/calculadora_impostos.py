from src.imposto.imposto import Imposto
from src.orcamento.orcamento import Orcamento


class CalculadoraImpostos:
    def calcular(self, orcamento: Orcamento, imposto: Imposto):
        return imposto.realizar_calculo_impostos(orcamento)
