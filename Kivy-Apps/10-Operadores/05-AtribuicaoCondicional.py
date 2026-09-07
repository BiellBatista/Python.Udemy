# -*- coding: utf-8 -*-
# Atribuição condicinal é a mesma coisa que oepração ternária

var = 10 if True else 20  # var rec rebe 10 se a condição for verdaidera e 20 se não for

num1 = int(input("Digite um número: "))
s = "par" if num1 % 2 == 0 else "impar"

print("O número digitado é %s" %s)
