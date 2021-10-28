from src.orcamento.orcavel import Orcavel
from src.orcamento.situacao.finalizado import Finalizado
from src.orcamento.situacao.situacao import Situacao
from src.orcamento.situacao.em_andamento import EmAndamento


class Orcamento(Orcavel):
    def __init__(self):
        self._valor = 0
        self._itens = []
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

    def is_finalizado(self):
        return isinstance(self.situacao, Finalizado)

    def adicionar_item(self, item: Orcavel):
        self._valor += item.valor
        self._itens.append(item)

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, novo_valor):
        self._valor = novo_valor

    @property
    def quantidade_itens(self):
        return len(self._itens)
