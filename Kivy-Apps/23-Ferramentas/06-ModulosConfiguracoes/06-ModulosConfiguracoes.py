'''
Config

Windows: c:\Users\Gabriel Batista\.kivy\config.ini
OS X: /Users/Gabriel Batista/.kivy/conifg.ini
Linux: /home/Gabriel Batista/.kivy/config.ini
ANDROID: /data/data/org.kivy.launcher/files/.kivy/config.ini
IOS: <HOME_DIRECTORY>/Documents/.kivy/config.ini
'''

# coding: utf-8

kv = """
<Inicio@StackLayout>:
    orientation: 'lr-tb'
    spacing: 5
    padding: 5

Inicio:

    Login:
        id: popup
        size_hint: 0.7, 0.4

<Login@Popup>:

    title: 'Login e Senha'
"""

import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.lang import Builder

class TelinhaApp(App):

    def build(self):
        return Builder.load_string(kv)

TelinhaApp().run()
