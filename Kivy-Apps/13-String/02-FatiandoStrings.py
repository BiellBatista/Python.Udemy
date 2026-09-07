# -*- coding: utf-8 -*-

# não é possível alterar ou deletar elementos de uma string, mas podemos fatiar a mesma

s = "Para o Python, toda String é uma lista imutável."

print(s)

p = s[0]  # pegando o primeiro elemento

print(p)  # não existe char no python. Aqui temos um elemento de uma lista de string, no caso a letra P

print(s[5:10])  # pegando as letras da possição 5 até a posisção 10
print(s[5:])  # pegando as letras da quinta possição até a última
print(s[::-1])  # invertendo uma palavra
print(s[::5])  # pegando as letras de cinco em cinco
