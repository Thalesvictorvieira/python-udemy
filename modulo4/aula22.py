#secrets gera numeros aleatorios seguros
# print(secrets.randbelow(100))
# print(secrets.choice([1,2,3,5,4]))
# o seed nao funciona com o secrets]
import secrets
import string as s
from secrets import SystemRandom as Sr

print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=64)))