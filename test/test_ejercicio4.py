import pytest
from src.ejercicio4 import filtrar_dia, filtrar_mes, filtrar_año

def test_filtrar_dia():
    assert filtrar_dia('3/11/2023') == '3'

    assert filtrar_dia('15/11/2023') == '15'

    assert filtrar_dia('1/11/2023') == '1'

def test_filtrar_mes():
    assert filtrar_mes('3/11/2023') == ('11/2023', '11')

    assert filtrar_mes('15/11/2023') == ('11/2023', '11')

    assert filtrar_mes('1/5/2023') == ('5/2023', '5')

def test_filtrar_año():
    assert filtrar_año('11/2023') == '2023'

    assert filtrar_año('05/2021') == '2021'

    assert filtrar_año('11/2005') == '2005'
