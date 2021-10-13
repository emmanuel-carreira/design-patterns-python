from src.desconto.calculadora_descontos import CalculadoraDescontos
from src.imposto.calculadora_impostos import CalculadoraImpostos
from src.imposto.icms import Icms
from src.orcamento.orcamento import Orcamento


def main():
    calcula_imposto()
    calcula_desconto()


def calcula_desconto():
    orcamento = Orcamento(600, 7)
    calculadora = CalculadoraDescontos()
    print(calculadora.calcular(orcamento))


def calcula_imposto():
    orcamento = Orcamento(100, 1)
    calculadora = CalculadoraImpostos()
    print(calculadora.calcular(orcamento, Icms()))


if __name__ == '__main__':
    main()
