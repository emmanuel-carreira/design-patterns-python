from src.desconto.calculadora_descontos import CalculadoraDescontos
from src.http.request_http import RequestHttp
from src.imposto.calculadora_impostos import CalculadoraImpostos
from src.imposto.icms import Icms
from src.imposto.iss import Iss
from src.orcamento.orcamento import Orcamento
from src.orcamento.registro_orcamento import RegistroOrcamento


def main():
    calcula_imposto()
    calcula_desconto()
    calcula_desconto_extra()
    registra_orcamento()


def calcula_desconto():
    orcamento = Orcamento(600, 7)
    calculadora = CalculadoraDescontos()
    print(calculadora.calcular(orcamento))


def calcula_imposto():
    orcamento = Orcamento(100, 1)
    calculadora = CalculadoraImpostos()
    print(calculadora.calcular(orcamento, Icms(Iss(None))))


def calcula_desconto_extra():
    orcamento = Orcamento(600, 7)
    orcamento.aplicar_desconto_extra()
    print(orcamento.valor)
    orcamento.aprovar()
    orcamento.aplicar_desconto_extra()
    print(orcamento.valor)


def registra_orcamento():
    orcamento = Orcamento(900, 5)
    orcamento.aprovar()
    orcamento.finalizar()
    registro_orcamento = RegistroOrcamento(RequestHttp())
    registro_orcamento.registrar(orcamento)


if __name__ == '__main__':
    main()
