from src.orcamento.situacao.finalizado import Finalizado
from src.orcamento.situacao.situacao import Situacao


class Reprovado(Situacao):
    def finalizar(self, orcamento):
        orcamento.situacao = Finalizado()
