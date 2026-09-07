# coding: utf-8

def erro(x):
    try:
        eval(x)
    except ValueError as e:  # associando a variável e a classe do tipo ValueError
        #print("ValueError")
        print(type(e))  # tipo
        #print(e.args)  # mensagem completa do erro
        #print(e)  # valor contido em e (__str__)
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except (TypeError, NameError) as e:  # com isso eu consigo tratar N exceções com o  mesmo trecho de código
        #print("TypeError ocorreu ou NameError")
        print(type(e))  # tipo
        #print(e.args)  # mensagem completa do erro
        #print(e)  # valor contido em e (__str__)
    else:
        print("Nenhuma exceção ocorreu.")
        '''
        TypeError ocorreu ou NameError
        <class 'TypeError'>
        ("unsupported operand type(s) for +: 'type' and 'type'",)
        unsupported operand type(s) for +: 'type' and 'type'
        TypeError ocorreu ou NameError
        <class 'NameError'>
        ("name 'a' is not defined",)
        name 'a' is not defined
        '''

# erro levantado do tipo TypeError
erro("int+int")

# erro levantado do tipo NameError
erro("a")

# erro levantando do tipo ValueError
erro("int('a')")

# erro levantando do tipo ZeroDivisionError
erro("5/0")

erro("10+10")
