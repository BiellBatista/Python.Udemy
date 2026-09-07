# -*- coding: utf-8 -*-
'''
def func():
    return 1, 2

a, b = func()

print(a, b)

t = (10, 20, 30)
a, b, c = t  # desempacotamento
print(a, b)
'''

def potencia(x):
    quadrado = x ** 2
    cubo = x ** 3

    return quadrado, cubo

q, c = potencia(2)

print(q)
print(c)
