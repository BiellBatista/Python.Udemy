#  -*- coding: utf-8 -*-

s = "Lista de Caracteres"

print(len(s))

ss = s.split(" ")  # dividindo a string toda vez que tiver um espaço em branco

print(ss)

lista = ss
listaNova = lista[0] + " " + lista[2]
print(listaNova)

listaNova1 = s.replace("de ", "")  # substituido os caracteres 'de' por ''
print(listaNova1)
