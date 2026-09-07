# coding: utf-8

def erro(x):
    try:
        eval(x)
    except TypeError:
        print("TypeError")
    except NameError:
        print("NameError")
    except ValueError:
        print("ValueError")
    except ZeroDivisionError:
        print("ZeroDivisionError")

# erro levantado do tipo TypeError
erro("int+int")

# erro levantado do tipo NameError
erro("a")
# erro levantando do tipo ValueError
erro("int('a')")
# erro levantando do tipo ZeroDivisionError
erro("5/0")
