from sympy import *

#Aclaración: Las operaciones deben estar sin espacios

def calculadora(palabra):

    operacion = ""
    original = palabra
    bandera_primera_operacion = True
    primera_operacion = ""
    hayParentesis = True
    i = 0
    while hayParentesis:
        palabra = original
        for i,x in enumerate(palabra):
            if x == "(":
                operacion = ""
            if x == ")":
                if operacion[len(operacion)-1:] == ')':
                    continue
                if operacion[0] != '(':
                    continue
                # Nos guardamos la primera operacion
                if bandera_primera_operacion == True:
                    primera_operacion = operacion[1:]
                    bandera_primera_operacion = False

                operacion += x
                original = original.replace(operacion, str(sympify(operacion)))
                operacion = ""
                
            operacion += x
        hayParentesis = False
        for x in original:
            if x == "(" or x == ")":
                hayParentesis = True
    
    return('(' + str(sympify(original)) + ', ' +primera_operacion + ')')