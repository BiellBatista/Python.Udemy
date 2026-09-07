# -*- coding: utf-8 -*-

lista = ['Cláudio', 'José', 'Maria', 'Beltrano', 'João', 'Fulano', 'Ciclano']

print(len(lista))  # quantidade de elementos
lista[-1]  # ultimo elemento
lista[-6]  # primeiro elemento
lista.insert(5, 'José')

lista.append('José')
print(lista)

qtd = lista.count('José')  # conta a quantidade de vezes que o elemento está na lista
print(qtd)

idc = lista.index('Maria')  # pega o indice do elemento X
print(idc)
idx = lista.index('José')
print(idx)