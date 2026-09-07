# coding: utf-8

from kivy.app import App
from kivy.uix.button import Button

def click():
    print("O botão foi clicado")

def build():
    bt = Button()
    bt.text = "Clique aqui"
    bt.on_press = click
    return bt

app = App()
app.build = build
app.run()
