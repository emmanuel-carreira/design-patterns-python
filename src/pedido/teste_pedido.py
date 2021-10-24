from src.pedido.acao.enviar_email import EnvioEmail
from src.pedido.acao.salvar_no_banco import SalvarBanco
from src.pedido.gera_pedido import GeraPedido
from src.pedido.gera_pedido_handler import GeraPedidoHandler


def teste_pedido(*args):
    cliente = args[0]
    valor = args[1]
    quantidade_itens = args[2]

    gera_pedido = GeraPedido(cliente, valor, quantidade_itens)
    invocador = GeraPedidoHandler([SalvarBanco(), EnvioEmail()])

    print("Espera a hora de processar...")
    invocador.executa(gera_pedido)


if __name__ == "__main__":
    teste_pedido("Emmanuel", 500, 3)
