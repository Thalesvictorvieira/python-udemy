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

valor_emprestimo = 1_000_000
data_pegou_emprestimo = datetime(2020,12,20)
numero_de_anos = relativedelta(years=5) #2025
data_pagar_emprestimo = data_pegou_emprestimo + numero_de_anos

dias_vinte = [] # vai receber todos os dias 20
data_para_modificar = data_pegou_emprestimo


while data_para_modificar < data_pagar_emprestimo:
    dias_vinte.append(data_para_modificar)
    data_para_modificar += relativedelta(months=+1)
   # print(f'A data de vencimento e {data_para_modificar} ')


numeros_parcela = len(dias_vinte)
valor_parcela = valor_emprestimo / numeros_parcela
print(f'Você pegou {valor_emprestimo}'
      f' para pagar em {numeros_parcela} meses'
      f' {numero_de_anos}'

      '')


    