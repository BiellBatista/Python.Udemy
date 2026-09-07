# -*- coding: utf-8 -*-

print("Antes de entrar no laço")

for item in range(10):
    print(item)
    if(item==6):
        print("A condição estabelecidade retornou true")
        break
print("Depois de ter entrado no laço")
