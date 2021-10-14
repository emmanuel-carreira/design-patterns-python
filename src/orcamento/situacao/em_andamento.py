from src.orcamento.situacao.aprovado import Aprovado
from src.orcamento.situacao.reprovado import Reprovado
from src.orcamento.situacao.situacao import Situacao


class EmAndamento(Situacao):
    def calcular_desconto_extra(self, orcamento):
        return orcamento.get_valor()*0.05

    def aprovar(self, orcamento):
        orcamento.situacao = Aprovado()

    def reprovar(self, orcamento):
        orcamento.situacao = Reprovado()
