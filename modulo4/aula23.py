import locale
from datetime import datetime
import string
locale.setlocale(locale.LC_ALL,'')

def converter_para_brl(numero: float| int) -> str:
    brl = 'R$' + locale.currency(val=numero,symbol=False,grouping=True)
    return brl

data = datetime.now()
dados = dict(
    nome='teste',
    valor=converter_para_brl(123456),
    data=data.strftime('%d/%m/%Y'),
    )
print(dados)

texto = """
ola teste $nome $valor $data 
"""
template = string.Template(texto)
print(template.safe_substitute()) 