from datetime import datetime

from src.pedido.pedido import Pedido
from src.orcamento.orcamento import Orcamento
from src.pedido.gera_pedido import GeraPedido


class GeraPedidoHandler:
    def __init__(self):
        # injeção de dependência para passar repository do banco e serviço de e-mail aqui
        pass

    def executa(self, dados: GeraPedido):
        orcamento = Orcamento(dados.valor, dados.quantidade_itens)
        pedido = Pedido(dados.cliente, orcamento, datetime.now())

        print("Salvar no banco...")
        print("Enviar e-mail com dados do pedido...")
