# -*- coding: utf-8 -*-

'''
lista_nums = [100, 200, 300, 400, 500, 600, 700, 800]
for item in range(len(lista_nums)):
    lista_nums[item] += 1000
print(lista_nums)
'''
lista_nums = [100, 200, 300, 400, 500, 600, 700, 800]
# a função enumerate() adiciona um indice para cada elemento de uma lista, fica tipo uma tupla
# não pode fazer operação matemática em cima da variável que estamos interando
for idx, item in enumerate(lista_nums):
    lista_nums[idx] += 1000
print(lista_nums)

