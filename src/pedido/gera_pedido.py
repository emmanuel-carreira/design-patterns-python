from datetime import datetime

from src.pedido.pedido import Pedido
from src.pedido.comando import Comando
from src.orcamento.orcamento import Orcamento


class GeraPedido(Comando):
    def __init__(self, cliente, valor, quantidade_itens):
        self.cliente = cliente
        self.valor = valor
        self.quantidade_itens = quantidade_itens

    def aplicar(self):
        orcamento = Orcamento(self.valor, self.quantidade_itens)
        pedido = Pedido(self.cliente, orcamento, datetime.now())

        print("Salvar no banco...")
        print("Enviar e-mail com dados do pedido...")
