import pytest
from src.ejercicio7 import lista_de_compra, calcular_precio

# def test_lista_de_compra(): ¿?¿?¿?¿?

def test_calcular_precio_con_productos():
    cesta_compra_test1 = {'Manzanas': 3.0, 'Naranjas': 2.5, 'Plátanos': 1.8}
    resultado1 = calcular_precio(cesta_compra_test1)
    assert resultado1 == 7.3

    cesta_compra_test3 = {'Manzanas': 3.0}
    resultado3 = calcular_precio(cesta_compra_test3)
    assert resultado3 == 3.0
   
