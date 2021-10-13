from src.desconto.desconto_mais_que_cinco_itens import DescontoMaisQueCincoItens
from src.desconto.desconto_valor_maior_que_quinhentos import DescontoValorMaiorQueQuinhentos
from src.desconto.sem_desconto import SemDesconto
from src.orcamento.orcamento import Orcamento


class CalculadoraDescontos:
    def calcular(self, orcamento: Orcamento):
        desconto = DescontoMaisQueCincoItens(
            DescontoValorMaiorQueQuinhentos(
                SemDesconto()
            )
        )
        return desconto.calcular(orcamento)