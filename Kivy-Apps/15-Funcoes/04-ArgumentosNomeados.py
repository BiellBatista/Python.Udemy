# -*- coding: utf-8 -*-

'''
POSICIONAIS X NOMEADOS
'''

def dados_pessoais(nome, sobrenome, idade, sexo):
    print("Nome: {}\nSobrenome: {}\nIdade: {}\nSexo: {}"
          .format(nome, sobrenome, idade, sexo))
# Argumento posicional
# dados_pessoais("Gabriel", "Batista", "21", "masculino")

# Argumento nomeados
dados_pessoais(idade="21", sexo=True, sobrenome="Batista", nome="Gabriel")

# quando defino um argumento como nomeado, os seguintes deverão ser nomeados