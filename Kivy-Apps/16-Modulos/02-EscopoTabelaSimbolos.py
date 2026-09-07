# -*- coding: utf-8 -*-

'''
Tabela de Símbolo são os nomes que podem ser usados no esocpo do módulo
Símbolo ou nome é toda e qualquer declaração. Seja uma variável, uma função, classe, etc.
Todo arquivo python é um modulo
'''

def func():
    print(__name__)  # o atributo __name__, retorna o nome da função (main)

a = 0

l = list()

for x in [1, 2]:
    b = 0

func()
# a variável a e o laço for estão no escopo global do módulo(arquivo)
# a variável b esta no escopo do laço for