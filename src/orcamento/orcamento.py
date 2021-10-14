from src.orcamento.situacao.situacao import Situacao
from src.orcamento.situacao.em_andamento import EmAndamento

class Orcamento:
    def __init__(self, valor, quantidade_itens):
        self.valor = valor
        self.quantidade_itens = quantidade_itens
        self._situacao = EmAndamento()

    @property
    def situacao(self):
        return self._situacao

    @situacao.setter
    def situacao(self, situacao: Situacao):
        self._situacao = situacao

    def aplicar_desconto_extra(self):
        self.valor -= self.situacao.calcular_desconto_extra(self)

    def aprovar(self):
        self.situacao.aprovar(self)

    def reprovar(self):
        self.situacao.reprovar(self)

    def finalizar(self):
        self.situacao.finalizar(self)

    def get_valor(self):
        return self.valor

    def get_quantidade_itens(self):
        return self.quantidade_itens
