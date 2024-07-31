import json
from pprint import pprint
string_json = '''
{
    "nome":"teste",
    "idadde":"18"
}    
'''

dados = json.loads(string_json)
print(dados['nome'])