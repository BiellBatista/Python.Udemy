# -*- coding: utf-8 -*-

'''
Exceção é todo o desvio da regra geral

Toda exceção é um objeto que herda da classe exception

Tratamento de Exceção: é todo código que identifica erros e implementa uma solução evitando que a aplicação seja finalizacada

Levantamento de Exceção: é todo código que ao perceber um problema cria uma exceção avisando o programador.

try:
    código
except ErroClass1:
    tratamento
except ErroClass2:
    trtamento
'''

try:
    a = 10 / 0
    print(a)
except ZeroDivisionError:
    print("Não é possível dividir um número por zero!")
