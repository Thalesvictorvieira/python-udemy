class MeuERROR(Exception):
    pass

def levantar():
    exception_ = MeuERROR('a','b','c')
    raise exception_
try:
    levantar()

except MeuERROR as error:
    print(error)