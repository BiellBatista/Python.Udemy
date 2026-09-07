# -*- coding: utf-8 -*-

'''
{right: 1.} indica que o componete deve ficar na extremidade direita (right = x + widthDoComponente)
{top: 1.} indica que o componente deve ficar na extremidade top (rop =  + height)
{center: 1.} defini a localização do componente com base no seu centro (center_x = x + (width/2))

    Button:
        pos_hint: {"top": 1.}


    FloatLayout:
        Button:
            rigth: 300 //origem na margem direita
            y: 0

        Button:
            right: 500
            y: 200

        Button:
            top: 100
            x: 0

        Button:
            top: 400
            x: 200

        Button:
            right: 500
            top: 200

        Button:
            center_x: 200
            center_y: 100

        Button:
            center_x: 200
            center_y: 300


    pos_hint: (dicionário)
    x
    y

    pos (tupla)
    right
    top

    center (tupla)
    center_x
    center_y
'''
