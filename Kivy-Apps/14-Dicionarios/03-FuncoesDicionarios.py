# -*- coding: utf-8 -*-

tel = {
    30301122: "Péricles",
    33547877: "Menelau",
    33381245: "Atreu",
    36458899: "Tieste"
}

print(tel)
print(36458899 in tel)  # verificando se o elemento etá no dicionario
print(len(tel))  # quantidade de elementos
del(tel[36458899])  # removendo elemento com a chave 36458899
print(tel)
print(tel.keys())  # retorna uma lista [] com as chaves
print(tel.values())  # retorna uma lista [] com os valores
print(tel.popitem())  # removendo um elemento, aleatoriamente, do dicionário e reetornando o mesmo

tel = {
    30301122: "Péricles",
    33547877: "Menelau",
    33381245: "Atreu",
    36458899: "Tieste"
}

tel2 = {
    99999999: "teste1",
    55551111: "teste2"
}

tel.update(tel2)  # adicionando todos os elementos de tel2 em tel

print(tel)

t = (10, 10, 10)
tel[t] = "eXcript"  # associando um valor em uma nova chave, eXcript é o valor a tupla é a chave

print(tel)
