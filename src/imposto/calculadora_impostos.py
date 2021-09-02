from src.imposto.tipo_imposto import TipoImposto
from src.orcamento.orcamento import Orcamento


class CalculadoraImpostos:
    def calcular(self, orcamento: Orcamento, tipo_imposto: TipoImposto):
        if tipo_imposto == TipoImposto.ICMS:
            return orcamento.get_valor() * 0.1
        elif tipo_imposto == TipoImposto.ISS:
            return orcamento.get_valor() * 0.06
        return 0
