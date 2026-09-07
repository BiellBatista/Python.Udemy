# -*- coding: utf-8 -*-

lista = [11, 10, 12]
tupla = 11, 10, 12

def func(a, b, c):
    print(a)
    print(b)
    print(c)

# lista.sort()
# func(*lista)

# l = [*tupla]
# l.sort()
# func(*l)

# A função zip(A, B) associa os elementos da tupla A, como chave dos elementos da tupla B
func(**dict(zip(("b", "a", "c"), lista)))
