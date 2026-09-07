# coding: utf-8

import kivy
kivy.require("1.9.1")

from kivy.app import App
from kivy.uix.button import Button

class OlaMundoApp(App):
    def build(self):
        return Button(text="Funcionou :D",
                      size_hint=(.2, .2),
                      pos_hint={"center_x": .5, "center_y": .5}
                      )

if __name__ == '__main__':
    OlaMundoApp().run()
