import pytest

from src.ejercicio2 import mensaje_datos_personales

def test_mensaje_datos_personales():
    assert mensaje_datos_personales('Juan', '25', 'Calle 123', '555-1234') == "Juan tiene 25 años, vive en Calle 123 y su numero de telefono es 555-1234"

    assert mensaje_datos_personales('Ana', '30', 'Calle 456', '555-5678') == "Ana tiene 30 años, vive en Calle 456 y su numero de telefono es 555-5678"
