# -*- coding: utf-8 -*-

num = 10
print(num)

# dentro de uma função, consigo ver os valores, mas não consigo alterar. Mas se eu colocar a palavra global,
# consigo alterar o valor de uma variável global
def func():
    num = 20  # isso não me dar acesso a variável global, porque não usei a palavra reservada global
    # global num #isso me dar a possibildiade de edtiar o valor de uma variavel global
    # a instrução global pode declarar uma variável no escopó global
    # ou seja, a insturção global me dar acesso a uma variável global ou criar uma variável global
    print(num)

func()
print(num)
