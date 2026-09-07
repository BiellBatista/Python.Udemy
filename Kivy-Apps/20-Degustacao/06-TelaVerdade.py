# coding: utf-8

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

ed = TextInput(text="eXcript")

def click():
    print(ed.text)

def build():
    # criando um layout para a janela
    layout = FloatLayout()

    ed.size_hint = None, None
    ed.height = 300
    ed.width = 400
    ed.x = 60
    ed.y = 250

    bt = Button(text="Click aqui")
    bt.size_hint = None, None
    bt.width = 200
    bt.height = 50
    bt.y = 150
    bt.x = 170
    bt.on_press = click

    layout.add_widget(ed)
    layout.add_widget(bt)

    return layout

janela = App()
janela.title = "Gabriel"

Window.size = 600, 600 # configurando tamanho da janela
janela.build = build
janela.run()
