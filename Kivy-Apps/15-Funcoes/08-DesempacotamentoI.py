# -*- coding: utf-8 -*-

# empacotar é adicionar valores em uma estrutura
# desempacotamento é a extração dos elementos contidos numa estrutura

'''
Os números  10 e 20 serão EMPACOTADOS
lista = [10, 20]
'''

lista = [10, 20]

def func(a, b):
    pass

func(*lista)  # o * serve para indicar que os valores contido numa lista, serão desempacotados
func(10, 20)  # mesma coisa q de cima
func(a=10, b=20)  # mesma coisa q de cima

def pessoa(nome, sobrenome, idade):
    print(nome)
    print(sobrenome)
    print(idade)

#tupla = "Gabriel", "Batista", 21
#pessoa(tupla[0], tupla[1], tupla[2])
#pessoa(*tupla)  #desempacotando a tupla

#lista = ["Gabriel", "Batista", 21]
#pessoa(*lista)  # desempacotando uma lista

d = { # posso fazer isso, porque os valores serão associados
    "sobrenome": "Batista",
    "idade": 21,
    "nome": "Gabriel",
}

#pessoa(*d)  #com um único * eu passo as chaves como os argumentos
pessoa(**d)  # com dois * eu passo os valores das chaves como argumentos