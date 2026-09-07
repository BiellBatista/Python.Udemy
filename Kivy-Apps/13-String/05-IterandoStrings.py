# -*- coding: utf-8 -*-

# EXEMPLO 1

# s = "Iterando Strings"
#
# for c in s:
#     print(c)

# EXEMPLO 2

# s = "Iterando Strings"
# indice = 0
#
# while indice < len(s):
#     print(indice, s[indice])
#     indice += 1

# EXEMPLO 3
s = "Iterando Strings"
#a função enumerate() relacionada um valor a uma chave(inteiro)
for k, v in enumerate(s):
    print(k, v)
