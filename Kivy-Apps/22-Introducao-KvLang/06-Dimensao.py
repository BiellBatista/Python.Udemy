# -*- coding: utf-8 -*-

'''
Dimensão Propriedades: as propriedades size_hin_x e size_hint_y definem as dimensões percentuais para cada eixo do plano

FloatLayout:
    Button:
        size_hint: (.8, .2)

    Button:
        size_hint_x: .5
        size_hint_y: .2

    Button:
        size_hint_x: None //informo que desejo determinar a largura em pixels
        size_hint_y: None
        width: 400 //pixels
        height: 200 //pixels

    Button:
        size_hint: (None, None)
        size: (400, 200)

    Button:
        size_hint: (None, None)
        width: 400 //pixels
        height: 200 //pixels
'''

'''
Propriedades Percentuais

size_hint (tupla)
size_hint_x
size_hint_y

Propriedades Absolutas
size (tupla)
width
height
'''
