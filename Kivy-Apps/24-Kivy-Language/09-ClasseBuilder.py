# -*- coding: utf-8 -*-

'''
A classe builder é usada pelo python para interpretar códigos kivy
'''

import kivy
kivy.require("1.9.1")
from kivy.app import App

# definindo hierarquira de componentes como string
code = """
BoxLayout:
    Button:
        text: "1"
    Button:
        text: "2"
"""

from kivy.lang import Builder

Builder.load_file('diretório') #lendo um arquivo que contenha um código kivy

class Estudo6App(App):
    def build(self):
        return Builder.load_string(code)  # rodando um código kivy que foi definido como string

janela = Estudo6App()
janela.run()
