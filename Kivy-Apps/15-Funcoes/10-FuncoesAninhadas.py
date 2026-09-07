# -*- coding: utf-8 -*-

def func():
    print("func")

    def func_interna():  # só posso invocar esta função, dentro da função func, porque ela foi definida aqui
        print("func_interna")
    func_interna()

func()
