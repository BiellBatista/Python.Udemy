# -*- coding: utf-8 -*-

'''
Propriedades com sufixo hint significam que os valores devem ser definidos em percentual.

Exemplo:
    - pos_hint: espera um dicionário com os eixos associados a valroes percentuais
    - size_hint

A propriedade pos recebe uma tupla onde o primeiro valor é atribuído à propriedade x e o segundo à propriedade y.
Exemplo:
    pos: 100, 350

    Button:
        pos_hint: {"x": .1, "y": .1}

    Button:
        x: 100
        y: 350

    Button:
        pos: 100, 350
'''
