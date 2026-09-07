# -*- coding: utf-8 -*-

'''
O Kivy possui três palavras reservadas

self - aponta para um componente (widget) que estã sendo editado. Ou seja, aponta pra si mesmo
root - aponta para para a classe (em pyhton ou em kivy) onde o componente (widget) está contido
app - aponta para a aplicação propriamente dita. Acessa a classe principal da aplicação
'''

import kivy
kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

def funcSelf(x):
    print("funcSelf")
Button.funcSelf = funcSelf

class MinhaTela(BoxLayout):
    def funcRoot(self):
        print("funcRoot")

class Estudo5App(App):
    def funcApp(self):
        print("funcApp")

janela = Estudo5App()
janela.run()
