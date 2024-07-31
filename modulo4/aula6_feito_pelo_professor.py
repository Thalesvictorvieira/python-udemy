# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
from datetime import datetime

from dateutil.relativedelta import relativedelta

valor_total = 1_000_000
data_emprestimo = datetime(2020, 12, 20)
delta_anos = relativedelta(years=5)
data_final = data_emprestimo + delta_anos

dia_20 = []
data_parcela = data_emprestimo
while data_parcela < data_final:
    dia_20.append(data_parcela)
    data_parcela += relativedelta(months=+1)
    print(data_parcela,'/'*20)

numero_parcelas = len(dia_20)
valor_parcela = valor_total / numero_parcelas

for data in dia_20:
    print(data.strftime('%d/%m/%Y'), f'R$ {valor_parcela:,.2f}')

print()
print(
    f'Você pegou R$ {valor_total:,.2f} para pagar '
    f'em {delta_anos.years} anos '
    f'({numero_parcelas} meses) em parcelas de '
    f'R$ {valor_parcela:,.2f}.'
)