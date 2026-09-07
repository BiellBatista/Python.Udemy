# -*- coding: utf-8 -*-

'''
É a instrução que permite acessar membros não globais e não locais, membros contidos no escopo externo
usado em funções aninhadas, ou seja, dar acesso a uma variável local de outra função
'''

def func():
    var_local = 10
    def func_inerna():
        nonlocal var_local
        var_local += 1
        print(var_local)
    func_inerna()

x = 10
def funcX():
    global x # faz eu acessar uma variável global
    x = 5
    return x

print(funcX())
print(x)
