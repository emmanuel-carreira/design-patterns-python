from src.http.http_adapter import HttpAdapter
from src.orcamento.orcamento import Orcamento


class RegistroOrcamento:
    def __init__(self, http_adapter: HttpAdapter):
        self.http_adapter = http_adapter

    def registrar(self, orcamento: Orcamento):
        if not orcamento.is_finalizado:
            raise Exception("Não é possível registrar orçamento não finalizado!")

        url = "http://api.externa/orcamento"
        dados = {"valor": orcamento.valor, "qtd_itens": orcamento.quantidade_itens}
        self.http_adapter.post(url, dados)
