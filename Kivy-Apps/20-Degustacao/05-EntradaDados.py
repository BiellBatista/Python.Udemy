# coding: utf-8

from kivy.app import App
from kivy.uix.textinput import TextInput

def build():
    #definindo uma entrada de dados com um texto padrão
    return TextInput(text = "Componente TextInput")

janela = App()
janela.build = build
janela.run()
