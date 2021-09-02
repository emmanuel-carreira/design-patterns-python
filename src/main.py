from src.imposto.calculadora_impostos import CalculadoraImpostos
from src.imposto.tipo_imposto import TipoImposto
from src.orcamento.orcamento import Orcamento


def main():
    orcamento = Orcamento(100)
    calculadora = CalculadoraImpostos()
    print(calculadora.calcular(orcamento, TipoImposto.ISS))


if __name__ == '__main__':
    main()
