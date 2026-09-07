# -*- coding: utf-8 -*-

'''
Recarregando um módulo em tempo de execução

O módulo pode ser recarregado. Porém, todos os valores definidos em seus membros serão perdidos
'''

# importlib é o módulo que contém diversas funcionalidades para manipular módulo
import importlib
import mod_a

del mod_a.b  # remove a variavel global 'b'
mod_a.a = 0

# reemportando o módulo mod_a
importlib.reload(mod_a)  # todas as modificações feitas neste módulo serão desfeitas

from pprint import pprint

pprint(mod_a.__dict__)
