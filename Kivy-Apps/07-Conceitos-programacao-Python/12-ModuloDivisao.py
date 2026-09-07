'''
print(6%2) #como em qualquer linguagen, o % serve para obter o resto de uma divisao
print(7%3.1) #0.79999999998
print(900%100==0) #True
'''

num1 = float(input("Digite um número: ")) #a função float() converte para float um numero
num2 = float(input("Digite outro número: "))

divisao = num1 / num2
resto = num1 % num2
print()
print(num1, "divido por", num2, "é igual a:", divisao)
print("O resto da divisao entre", num1, "e", num2, "é igual a:", resto)
