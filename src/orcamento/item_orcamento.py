from src.orcamento.orcavel import Orcavel


class ItemOrcamento(Orcavel):
    def __init__(self, nome, valor):
        self._nome = nome
        self._valor = valor

    @property
    def valor(self):
        return self._valor
