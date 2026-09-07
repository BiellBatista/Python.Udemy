# -*- coding: utf-8 -*-

# lista[start:stop:step]
# por padrao o start eh 0, o stop eh len() e o step eh 1
# lista[::-1] invete uma lista

lista = "Bem-vindo ao Curso de Python"
print(lista[:20])  # vai de zero até 20 um por vez
print(lista[10:20])  # vai de 10 até 20 um por vez
print(lista[::2])  # vai do inicio ate o fim de dois em dois
print(lista[::-1])  # inverte a lista
