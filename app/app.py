# app/app.py
"""
Aplicación web de calculadora usando Flask.

Esta aplicación proporciona una interfaz web para realizar
operaciones matemáticas básicas (suma, resta, multiplicación y división)
usando Flask como framework web.
"""

import os
from flask import Flask, render_template, request
from .calculadora import sumar, restar, multiplicar, dividir

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Ruta principal que maneja la interfaz de la calculadora.

    Maneja las solicitudes:
    - GET (mostrar formulario)
    - POST (procesar cálculo).
    Procesa las operaciones matemáticas y maneja errores de validación.

    Returns:
        str: Respuesta HTML renderizada con el resultado del cálculo o errores.
    """
    resultado = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operacion = request.form["operacion"]

            if operacion == "sumar":
                resultado = sumar(num1, num2)
            elif operacion == "restar":
                resultado = restar(num1, num2)
            elif operacion == "multiplicar":
                resultado = multiplicar(num1, num2)
            elif operacion == "dividir":
                resultado = dividir(num1, num2)
            else:
                resultado = "Operación no válida"
        except ValueError:
            resultado = "Error: Introduce números válidos"
        except ZeroDivisionError:
            resultado = "Error: No se puede dividir por cero"

    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":  # pragma: no cover
    debug_env = os.environ.get("FLASK_DEBUG", "False").lower()
    debug_mode = debug_env in ["true", "1", "yes"]
    app.run(debug=debug_mode, port=5000, host="0.0.0.0")
