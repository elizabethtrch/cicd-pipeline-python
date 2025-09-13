# app/calculadora.py
"""
Módulo de funciones matemáticas básicas.
"""


def sumar(a, b):
    """
    Suma dos números.

    Args:
        a (float): Primer número.
        b (float): Segundo número.

    Returns:
        float: La suma de a y b.
    """
    return a + b


def restar(a, b):
    """
    Resta dos números.

    Args:
        a (float): Primer número.
        b (float): Segundo número.

    Returns:
        float: El resultado de a menos b.
    """
    return a - b


def multiplicar(a, b):
    """
    Multiplica dos números.

    Args:
        a (float): Primer número.
        b (float): Segundo número.

    Returns:
        float: El producto de a y b.
    """
    return a * b


def dividir(a, b):
    """
    Divide dos números y maneja la división por cero.

    Args:
        a (float): Numerador.
        b (float): Denominador.

    Raises:
        ZeroDivisionError: Si b es cero.

    Returns:
        float: El resultado de a dividido por b.
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")

    return a / b
