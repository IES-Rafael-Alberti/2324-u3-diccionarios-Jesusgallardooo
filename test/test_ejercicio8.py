import pytest

from src.ejercicio8 import dividir_palabras_frase, separar_palabra_traduccion

def test_separar_palabra_traduccion():
    resultado1 = separar_palabra_traduccion("hello:hola")
    assert resultado1 == ("hello", "hola")

    resultado2 = separar_palabra_traduccion("apple : manzana")
    assert resultado2 == ("apple", "manzana")


def test_dividir_palabras_frase():
    resultado1 = dividir_palabras_frase("Hola cómo estás")
    assert resultado1 == ["Hola", "cómo", "estás"]

    resultado2 = dividir_palabras_frase("Juan, siempre igual.")
    assert resultado2 == ["Juan,", "siempre", "igual."]