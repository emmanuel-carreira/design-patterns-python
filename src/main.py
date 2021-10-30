from src.desconto.calculadora_descontos import CalculadoraDescontos
from src.http.request_http import RequestHttp
from src.imposto.calculadora_impostos import CalculadoraImpostos
from src.imposto.icms import Icms
from src.imposto.iss import Iss
from src.orcamento.item_orcamento import ItemOrcamento
from src.orcamento.orcamento import Orcamento
from src.orcamento.orcamento_proxy import OrcamentoProxy
from src.orcamento.registro_orcamento import RegistroOrcamento


def main():
    calcula_imposto()
    calcula_desconto()
    calcula_desconto_extra()
    registra_orcamento()
    compoe_orcamento()


def calcula_desconto():
    orcamento = Orcamento()
    orcamento.adicionar_item(ItemOrcamento('Mouse', 100))
    orcamento.adicionar_item(ItemOrcamento('Fone de ouvido', 20))
    orcamento.adicionar_item(ItemOrcamento('Teclado', 100))
    orcamento.adicionar_item(ItemOrcamento('Suporte de celular', 30))
    orcamento.adicionar_item(ItemOrcamento('Mousepad', 50))
    orcamento.adicionar_item(ItemOrcamento('Caixas de som', 50))
    orcamento.adicionar_item(ItemOrcamento('Headset', 250))
    calculadora = CalculadoraDescontos()
    print(calculadora.calcular(orcamento))


def calcula_imposto():
    orcamento = Orcamento()
    orcamento.adicionar_item(ItemOrcamento('Mouse', 100))
    calculadora = CalculadoraImpostos()
    print(calculadora.calcular(orcamento, Icms(Iss(None))))


def calcula_desconto_extra():
    orcamento = Orcamento()
    orcamento.adicionar_item(ItemOrcamento('Mouse', 100))
    orcamento.adicionar_item(ItemOrcamento('Fone de ouvido', 20))
    orcamento.adicionar_item(ItemOrcamento('Teclado', 100))
    orcamento.adicionar_item(ItemOrcamento('Suporte de celular', 30))
    orcamento.adicionar_item(ItemOrcamento('Mousepad', 50))
    orcamento.adicionar_item(ItemOrcamento('Caixas de som', 50))
    orcamento.adicionar_item(ItemOrcamento('Headset', 250))
    orcamento.aplicar_desconto_extra()
    print(orcamento.valor)
    orcamento.aprovar()
    orcamento.aplicar_desconto_extra()
    print(orcamento.valor)


def registra_orcamento():
    orcamento = Orcamento()
    orcamento.adicionar_item(ItemOrcamento('Mouse', 200))
    orcamento.adicionar_item(ItemOrcamento('Teclado', 200))
    orcamento.adicionar_item(ItemOrcamento('Suporte de celular', 50))
    orcamento.adicionar_item(ItemOrcamento('Caixas de som', 50))
    orcamento.adicionar_item(ItemOrcamento('Headset', 400))
    orcamento.aprovar()
    orcamento.finalizar()
    registro_orcamento = RegistroOrcamento(RequestHttp())
    registro_orcamento.registrar(orcamento)


def compoe_orcamento():
    orcamento_antigo = Orcamento()
    orcamento_antigo.adicionar_item(ItemOrcamento('Celular', 1000))
    orcamento_antigo.reprovar()

    orcamento_novo = OrcamentoProxy()
    orcamento_novo.adicionar_item(ItemOrcamento('Fone de ouvido', 100))
    orcamento_novo.adicionar_item(orcamento_antigo)
    print(orcamento_novo.valor)
    print(orcamento_novo.valor)


if __name__ == '__main__':
    main()
