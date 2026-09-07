# -*- coding: utf-8 -*-

# para importar um símbolo privado, é necessário invocá-lo explicitamente
# o * serve para importar todos os símbolos não privado
from Ferramentas import *
# importando um simbolo privado
from Ferramentas import _a
from pprint import pprint

pprint(globals())
print(_a)
