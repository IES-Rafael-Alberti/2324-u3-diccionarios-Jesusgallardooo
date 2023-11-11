import pytest

from src.ejercicio3 import calcular_precio_frutas

precios_frutas_test = {'manzana': 2.0, 'banana': 1.5, 'uva': 3.0}


def test_calcular_precio_frutas():

    assert calcular_precio_frutas('manzana', 3, precios_frutas_test) == 6.0

    assert calcular_precio_frutas('kiwi', 2, precios_frutas_test) == 0

    assert calcular_precio_frutas('banana', 0, precios_frutas_test) == 0
