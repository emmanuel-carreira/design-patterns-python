from src.pedido.pedido import Pedido
from src.pedido.acao.acao import Acao


class SalvarBanco(Acao):
    def executar_acao(self, pedido: Pedido):
        print("Salvar no banco...")
