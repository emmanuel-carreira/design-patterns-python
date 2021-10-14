from src.desconto.calculadora_descontos import CalculadoraDescontos
from src.imposto.calculadora_impostos import CalculadoraImpostos
from src.imposto.icms import Icms
from src.orcamento.orcamento import Orcamento


def main():
    calcula_imposto()
    calcula_desconto()
    calcula_desconto_extra()


def calcula_desconto():
    orcamento = Orcamento(600, 7)
    calculadora = CalculadoraDescontos()
    print(calculadora.calcular(orcamento))


def calcula_imposto():
    orcamento = Orcamento(100, 1)
    calculadora = CalculadoraImpostos()
    print(calculadora.calcular(orcamento, Icms()))


def calcula_desconto_extra():
    orcamento = Orcamento(600, 7)
    orcamento.aplicar_desconto_extra()
    print(orcamento.valor)
    orcamento.aprovar()
    orcamento.aplicar_desconto_extra()
    print(orcamento.valor)


if __name__ == '__main__':
    main()
