# -*- coding: utf-8 -*-

# d1 = {} criando um dicionario
# d2 = dict()   criando um dicionario

d1 = {}
d1['aaa'] = 1000
d1['bbb'] = 2000
d1['ccc'] = 3000

print(d1)  # {'aaa': 1000, 'bbb': 2000, 'ccc': 3000} Dados dentro de {} significa dicionario
print(d1['bbb'])  # 2000

d2 = {1.1: "teste1", 2.2: "teste2", 3: "teste3"}
print(d2)  # {1.1: 'teste1', 2.2: 'teste2', 3: 'teste3'}
print(d2[2.2])  # teste2
