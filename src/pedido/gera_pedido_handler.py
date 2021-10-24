from datetime import datetime
from typing import List

from src.pedido.pedido import Pedido
from src.pedido.gera_pedido import GeraPedido
from src.pedido.acao.acao import Acao
from src.orcamento.orcamento import Orcamento

class GeraPedidoHandler:
    def __init__(self, acoes: List[Acao]):
        self.acoes = acoes

    def executa(self, dados: GeraPedido):
        orcamento = Orcamento(dados.valor, dados.quantidade_itens)
        pedido = Pedido(dados.cliente, orcamento, datetime.now())
        self._notifica_criacao_de_pedido(pedido)

    def _notifica_criacao_de_pedido(self, pedido):
        for acao in self.acoes:
            acao.executar_acao(pedido)
