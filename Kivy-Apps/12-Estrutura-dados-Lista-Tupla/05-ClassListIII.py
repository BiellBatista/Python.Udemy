# -*-  coding: utf-8 -*-

lista = [1, 2, 3, 4, 5]

print(lista) # [1, 2, 3, 4, 5]

lista = lista + [6]  # concatenando listas
lista += [7, 8, 9, 10]  #
print(lista)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista = [0] + lista  #  concatenando listas

print(lista)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista.append(11)  # adicionando elemento na lista
print(lista)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

lista.append([11])  # adicionando lista na lista
print(lista)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, [11]]

del(lista[-1])  # excluindo o último elemento de uma lista
print(lista)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

elemento = 10 * [0]  # criando uma lsita com 10 elementos iguais a zero
lista += 10 * [0]  # adicionando dez elementos iguais a zero na lista
print(lista)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print(2 * "=")  # pritando duas vezes o sinal =
