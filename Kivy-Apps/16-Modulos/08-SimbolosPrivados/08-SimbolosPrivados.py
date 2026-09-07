# -*- coding: utf-8 -*-

# para importar um símbolo privado, é necessário invocá-lo explicitamente
# o * serve para importar todos os símbolos não privado
from Ferramentas_08 import *
# importando um simbolo privado
from Ferramentas_08 import _a
from pprint import pprint

pprint(globals())
print(_a)
