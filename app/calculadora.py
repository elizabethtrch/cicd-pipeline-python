# app/calculadora.py
def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    """
    funcion para dividir dos numeros (a y b)
    y manejar la division por cero
    si b es cero, lanza una excepcion
    si no, retorna la division
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b
