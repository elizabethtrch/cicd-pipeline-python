# app/app.py
"""
Aplicación web de calculadora usando Flask.

Esta aplicación proporciona una interfaz web para realizar
operaciones matemáticas básicas (suma, resta, multiplicación y división)
usando Flask como framework web.
"""

import os
from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from .calculadora import sumar, restar, multiplicar, dividir

DEV_SECRET_KEY = "dev-secret-key-change-in-production"
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("CSRF_SECRET_KEY", DEV_SECRET_KEY)
csrf = CSRFProtect(app)
app_port = int(os.environ.get("PORT", 5000))
DEBUG_ENV = os.environ.get("FLASK_DEBUG", "False").lower()
DEBUG_MODE = DEBUG_ENV in ["true", "1", "yes"]
app.debug = DEBUG_MODE

@app.route("/health")
def health():
    return "OK", 200


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
    app.run(debug=DEBUG_MODE, port=5000, host="0.0.0.0")
