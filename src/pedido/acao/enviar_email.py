from src.pedido.pedido import Pedido
from src.pedido.acao.acao import Acao


class EnvioEmail(Acao):
    def executar_acao(self, pedido: Pedido):
        print("Enviar e-mail com dados do pedido...")
