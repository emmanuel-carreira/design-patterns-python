from src.orcamento.orcamento import Orcamento


class Imposto:
    def __init__(self, outro_imposto):
        self.outro_imposto = outro_imposto

    def calcular(self, orcamento: Orcamento):
        raise NotImplementedError

    def realizar_calculo_impostos(self, orcamento: Orcamento):
        valor_imposto = self.calcular(orcamento)
        valor_outro_imposto = self.outro_imposto.calcular(orcamento) if self.outro_imposto else 0
        return valor_imposto + valor_outro_imposto
