from src.imposto.calculadora_impostos import CalculadoraImpostos
from src.imposto.icms import Icms
from src.orcamento.orcamento import Orcamento


def main():
    orcamento = Orcamento(100)
    calculadora = CalculadoraImpostos()
    print(calculadora.calcular(orcamento, Icms()))


if __name__ == '__main__':
    main()
