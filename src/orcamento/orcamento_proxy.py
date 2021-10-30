from src.orcamento.orcamento import Orcamento


class OrcamentoProxy(Orcamento):
    @property
    def valor(self):
        if not self._valor:
            self._valor = super().valor
        return self._valor
