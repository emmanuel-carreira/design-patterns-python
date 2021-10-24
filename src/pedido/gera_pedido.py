from datetime import datetime

from src.pedido.pedido import Pedido
from src.orcamento.orcamento import Orcamento


class GeraPedido:
    def __init__(self, cliente, valor, quantidade_itens) -> None:
        self.cliente = cliente
        self.valor = valor
        self.quantidade_itens = quantidade_itens

    def executa(self):
        orcamento = Orcamento(self.valor, self.quantidade_itens)
        pedido = Pedido(self.cliente, orcamento, datetime.now())

        print("Salvar no banco...")
        print("Enviar e-mail com dados do pedido...")
