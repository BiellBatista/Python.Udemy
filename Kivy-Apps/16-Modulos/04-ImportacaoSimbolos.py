# -*- coding: utf-8 -*-

"""
A Importação de Símbolos copia atributos de um módulo diretamente à tabela de símbolos local

Posso importar módulos e simbolos em funções, laços e etc..
"""
#a partir deste módulo, importe estes símbolos
#form modulo import simbolo1, simbolo2

#importe o modulo com o apelido M
#import modulo as M

#a partir do modulo, importe simb1 com o apelido de s1 e simb2 com o apelido de s2
#form modulo import simb1 as s1, simb2 as s2

#importanto todos os simbolos de um modulo
#from modulo import *

from math import pi, e
from math import sqrt

print(pi)
print(e)

print(sqrt(pi))

def func():
    from math import factorial
    print(factorial(10))

func()
