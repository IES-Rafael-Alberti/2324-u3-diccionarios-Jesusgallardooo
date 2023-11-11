import pytest
from src.ejercicio9 import calcular_pago_pendiente, calcular_cobro_hecho, eliminar_factura_de_diccionario

def test_calcular_pago_pendiente():
    facturas_test1 = {'1': 100.0, '2': 150.0, '3': 200.0}
    cantidad_pendiente_test1, cantidad_cobrada_test1 = calcular_pago_pendiente(facturas_test1, 0, 0, '2')
    assert cantidad_pendiente_test1 == 150.0
    assert cantidad_cobrada_test1 == 0

    facturas_test2 = {'1': 100.0, '2': 150.0, '3': 200.0}
    cantidad_pendiente_test2, cantidad_cobrada_test2 = calcular_pago_pendiente(facturas_test2, 50.0, 0, '3')
    assert cantidad_pendiente_test2 == 250.0
    assert cantidad_cobrada_test2 == 0

def test_calcular_cobro_hecho():
    cantidad_pendiente_test1, cantidad_cobrada_test1 = calcular_cobro_hecho(0, 0, 100.0)
    assert cantidad_pendiente_test1 == -100.0  
    assert cantidad_cobrada_test1 == 100.0

    cantidad_pendiente_test2, cantidad_cobrada_test2 = calcular_cobro_hecho(50.0, 30.0, 20.0)
    assert cantidad_pendiente_test2 == 30.0
    assert cantidad_cobrada_test2 == 50.0


def test_eliminar_factura_de_diccionario():
    facturas_test1 = {'1': 100.0, '2': 150.0, '3': 200.0}
    eliminar_factura_de_diccionario(facturas_test1, '2')
    assert 'factura2' not in facturas_test1
    assert len(facturas_test1) == 2




