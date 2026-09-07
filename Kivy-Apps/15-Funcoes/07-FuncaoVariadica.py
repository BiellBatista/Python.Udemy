# -*- coding: utf-8 -*-

# Funcção variádica é toda função capaz de receber quantidades arbitrárias de parâmetros,
# tanto possicionado, quanto nomeados

'''
def func(*args, **kwargs):
    pass

argumentos com um *, significa N argumentos possicionados
argumentos com dois **, significa N argumentos associativos (nomeados)
'''

def lista_de_argumentos(*lista):
    print(lista)

def lista_de_argumentos_associativos(**dicionario):
    print(dicionario)

# primeiro vem os possicionais, depois os chaves valor
def argumentos(*args, **kwargs):
    print(args)
    print(kwargs)

argumentos(1, 2, 3, 4, um = 1, dois = 2, tres = 3)

lista_de_argumentos(1, 2, 3, 4, 5, 6)  # manda uma tupla
lista_de_argumentos("um", "dois", "três", "quatro")  # manda uma tupla

lista_de_argumentos_associativos(nome="Gabriel", sobrenome="Batista", idade=21)  # manda um dicionario
