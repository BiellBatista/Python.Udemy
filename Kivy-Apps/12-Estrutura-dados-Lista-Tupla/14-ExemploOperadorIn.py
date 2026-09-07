#  -*- coding: utf-8 -*-

# a = 10
# b = 25
# c = 66
#
# x = int(input("Digite um número: "))
#
# if (x == a or a == b or x == c):
#     print("Está contido")
# else:
#     print("Não está contido")
#
# #  uma forma mais agradável de verificar se um valor está no esperado
# if (x in [a, b, c]):
#     print("Está contido")
# else:
#     print("Não está contido")
#--------------------------------------------------------------------------

cores = ["azul", "amarelo", "vermelho", "branco"]

while True:
    cor = input("Digite o nome de uma cor ou então 0 para sair do programa: ")

    if (cor == "0"):
        break
    elif (cor.lower in cores):
        print("Essa cor está contida!")
    else:
        print("Essa cor não está contida!")
