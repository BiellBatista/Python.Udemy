# -**- coding: utf-8 -*-

import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

# esta classe é para gerenciar o layout
class Tela1(BoxLayout):
    def __init__(self, **kwargs):
        super(Tela1, self).__init__(**kwargs)
        self.orientation = "vertical"
        bt1 = Button(text="Clique")
        bt1.on_press = self.on_press_bt  # sem os () associamos a função ao evento e com () invocamos ela
        self.add_widget(bt1)
        self.add_widget(Button(text="bt2"))
        self.add_widget(Button(text="bt3"))

    # define o topo da hierarquia
    def on_press_bt(self):
        janela.root_window.remove_widget(janela.root)  # remove a janela do topo
        janela.root_window.add_widget(Tela2())  # adiciona nova jenale ao topo

class Tela2(BoxLayout):
    def __init__(self, **kwargs):
        super(Tela2, self).__init__(**kwargs)
        self.orientation = "vertical"
        bt = Button(text="Click")
        bt.on_press = self.on_press_bt
        self.add_widget(bt)

    def on_press_bt(self):
        janela.root_window.remove_widget(janela.root)
        janela.root_window.add_widget(Tela1())

class KVvsPY(App):
    def build(self):
        return Tela1()  # topo da hieraquia

janela = KVvsPY()
janela.run()
