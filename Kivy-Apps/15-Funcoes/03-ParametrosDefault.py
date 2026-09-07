# -*- coding: utf-8 -*-

'''
default são parâmetros que recebem um valor na declaração, com isso ele se torna facultativo. A única regra é que
eles deverão ser os últimos a ser definidos na declaração
'''

def login(sistema, usuario="root", senha="123"):
    print("Usuário: %s \nSenha: %s" %(usuario, senha))

login("OI")
