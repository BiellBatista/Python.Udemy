# -**- coding: utf-8 -*-

from tkinter import Widget

import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

# esta classe é para gerenciar o layout
class Tela1(BoxLayout):
    # define o topo da hierarquia
    def on_press_bt(self):
        janela.root_window.remove_widget(janela.root)  # remove a janela do topo
        janela.root_window.add_widget(Tela2())  # adiciona nova jenale ao topo

class Tela2(BoxLayout):
    def on_press_bt(self):
        janela.root_window.remove_widget(janela.root)
        janela.root_window.add_widget(Tela1())

class KVvsPY2(App):  # esta classe deve ter o mesmo nome que o arquivo .kv, porque ela é a principal
#  chamo a classe instanciada no arquivo .kv
    def build(self):
        return Tela1()  # topo da hieraquia

janela = KVvsPY2()
janela.run()
