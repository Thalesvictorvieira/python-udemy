# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.
from functools import partial

class Foo:
    def __init__(self) :
        self.public = ' Isso e publico'
        self._preotected = 'Isso e protegido'
        self.__private = 'ISSO E PRIVADO'
    
    def metedo_publico(self):
        return 'metodo_publico'

    def _metedo_protected(self):
        print('_metedo_protected')
        return '_metedo_protected'
    
    def __metodo_Privado(self):
        print('__metedo_privado')
        return '__metedo_privado'


f = Foo()

print(f._Foo__metodo_Privado())