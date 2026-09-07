# -*- coding: utf-8 -*-

# Widget são todos os elementos (componentes) visuais e gerenciadores de eventos
# KvLang é uma linguagem de marcação definida pelo grupo responsável pelo framework Kivy
# Kivy Lang é uma linguagem de marcação no estilo QML, XML e JSON com o objetivo de separar o código de interface visual do código da lógica de negócio

'''
Estrutura de uma janela no Kivy
<ClassName>: --widget master
    LayoutType: gerenciador de widget
        WidgetType: widget
            pos: 10, 10
            size: .5, .5

    LayoutType2: gerenciador de widget / widget
        font_size: 70
        center_x: root.width / 4
        top: root.top - 5
        texto: "0"
'''
