import pytest

from src.ejercicio10 import almacenar_clientes, comprobar_ausencia, listar_clientes, listar_clientes_preferentes

#def test_almacenar_clientes(): ¿?¿?¿?¿?

#def test_comprobar_ausencia(clientes_prueba, capsys): ¿?¿?¿?¿¿?¿?


def test_listar_clientes(clientes_prueba):
    lista_clientes = listar_clientes(clientes_prueba)
    assert len(lista_clientes) >= 1

#def test_listar_clientes_preferentes(): ¿?¿?¿?¿?¿?¿?¿?

