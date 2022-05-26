inicio = True
while inicio == True:
    lista = []
    valor = input("     Ingresar valor ('fin' para finalizar):")

    while valor != "fin":
        lista.append(int(valor))
        valor = input("     Ingresar valor ('fin' para finalizar):")

    print("     ¿Que desea hacer con? >>",lista,)
    print("     s para Sumar    r para Restar   m para Multiplicar  off para Apagar")
    opcion = input("        >> ")

    if opcion == "s":
        def Sum(*arg):
            Var = 0
            for i in arg:
                var = tuple(i)
                for y in var:
                    Var += y
            return Var
        print("     ",lista," El resultado es:",Sum(lista))

    elif opcion == "m":
        def Mult(*arg):
            Var = 1
            for i in arg:
                var = tuple(i)
                for y in var:
                    Var *= y
            return Var
        print("     ",lista," El resultado es:",Mult(lista))

    elif opcion == "r":
        def Res(*arg):
            Var = 0
            for i in arg:
                var = tuple(i)
                for y in var:
                    Var -= y
            return Var
        print("     ",lista," El resultado es:",Res(lista))

    elif opcion == "off":
            inicio = False