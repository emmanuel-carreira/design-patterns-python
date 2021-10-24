from src.pedido.pedido import Pedido


class Acao:
    def executar_acao(self, pedido: Pedido):
        raise NotImplementedError
