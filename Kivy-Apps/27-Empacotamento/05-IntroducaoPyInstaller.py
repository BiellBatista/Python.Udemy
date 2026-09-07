# -*- coding: utf-8 -*-

'''
PyInstaller faz empacotamento de uma aplicação escrita em python

O PyInstaller disponibiliza duas formas de empatocamento

1 - onefile: gera um único executável que contenha um único arquivo (tem divesos problemas)
2 - onedir: gera uma única pasta

Devo usar o PyInstaller 3
Para empacotar para o raspberry pi, devo realizar o empacotamento no raspberry, porque o empacotamento é realizado com base no sistema

Principais Características
1 - O executável servirá apenas para o SO em que foi gerado
2 - A quantidade de bits do Python definirá os bits do SO
3 - O executável suportará a versão atual e posteriores do SO
4 - A versão do Python é indiferente
5 - Instalação do Python limpa
6 - Instalação do SO limpa
'''
