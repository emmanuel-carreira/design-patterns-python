from .gera_pedido import GeraPedido
from .invocador import Invocador

def teste_pedido(*args):
    cliente = args[0]
    valor = args[1]
    quantidade_itens = args[2]

    gera_pedido = GeraPedido(cliente, valor, quantidade_itens)
    invocador = Invocador(gera_pedido)

    print("Espera a hora de processar...")
    invocador.executar()


if __name__ == "__main__":
    teste_pedido("Emmanuel", 500, 3)
