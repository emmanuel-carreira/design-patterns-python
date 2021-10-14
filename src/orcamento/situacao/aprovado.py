from src.orcamento.situacao.finalizado import Finalizado
from src.orcamento.situacao.situacao import Situacao


class Aprovado(Situacao):
    def calcular_desconto_extra(self, orcamento):
        return orcamento.get_valor()*0.02

    def finalizar(self, orcamento):
        orcamento.situacao = Finalizado()
