# -*- coding: utf-8 -*-

print(2 in (1, 2, 3, 4, 5))  # o operador in verifica se um valor está contido  em uma lista ou tupla ou dicionário

print(6 not in (1, 2, 3, 4, 5))  # o operador not in verifica se um valor não está contido em uma lista ou tupla ou dicionário

print(1 in range(1, 6,))

print(1 in range(1, 6))

x = range(1, 6)

if 3 in x:
    print("Contido")
else:
    print("Não está contido")
