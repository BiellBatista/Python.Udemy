# -*- coding: utf-8 -*-

l = ['bbb', 'ccc', 'ddd']
print(l)

l.append('eee')  # adicionando elemento no fim da lista
print(l)

l.insert(0, 'aaa') # adiciona elemento em uma possição, neste caso o 0
print(l)

l.clear()  # limpando lista

l = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
print(l.pop()) # remove o último elemento da lista e retorna o mesmo

print(l.pop(0))  # remove o elemento de indice 0, poderia ser qualquer um

del(l[2:4])  # apagando os elementos de 2 a 4
