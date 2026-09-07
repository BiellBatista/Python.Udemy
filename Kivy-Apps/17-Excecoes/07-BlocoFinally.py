# coding: utf-8

def erro(x):
    try:
        eval(x)
    except ValueError as e:
        print(type(e))
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except (TypeError, NameError) as e:
        print(type(e))
    else:
        print("Nenhuma exceção ocorreu.")
    finally:
        print("Sempre será executado.")

# erro levantado do tipo TypeError
erro("int+int")

# erro levantado do tipo NameError
erro("a")

# erro levantando do tipo ValueError
erro("int('a')")

# erro levantando do tipo ZeroDivisionError
erro("5/0")

erro("10+10")
