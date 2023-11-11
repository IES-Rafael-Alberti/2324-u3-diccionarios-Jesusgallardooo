import pytest
from src.ejercicio6 import nombrar_dato, introducir_valor_dato, guardar_dato

def test_nombrar_dato(monkeypatch):
    # Simular entrada de usuario usando monkeypatch
    input_usuario = "Nombre"
    monkeypatch.setattr('builtins.input', lambda _: input_usuario)
    
    # Ejecutar la función y verificar el resultado
    resultado = nombrar_dato()
    assert resultado == input_usuario


def test_introducir_valor_dato(monkeypatch):
    # Simular entrada de usuario usando monkeypatch
    input_usuario = "18"
    monkeypatch.setattr('builtins.input', lambda _: input_usuario)

    # Ejecutar la función y verificar el resultado
    resultado = introducir_valor_dato("edad")
    assert resultado == input_usuario


def test_guardar_dato():
    # Caso de prueba 1: Dato y valor válidos
    datos_personales_test1 = {}
    guardar_dato(datos_personales_test1, "nombre", "Juan")
    assert datos_personales_test1 == {"nombre": "Juan"}

    datos_personales_test3 = {"telefono": "555-1234"}
    guardar_dato(datos_personales_test3, "correo", "juan@example.com")
    assert datos_personales_test3 == {"telefono": "555-1234", "correo": "juan@example.com"}