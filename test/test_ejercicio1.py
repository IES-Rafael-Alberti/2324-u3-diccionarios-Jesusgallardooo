import pytest

from src.ejercicio1 import detectar_simbolo_divisa

monedas_test = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}

def test_detectar_simbolo_divisa():
    assert detectar_simbolo_divisa(monedas_test, 'Dollar') == '$'

    assert detectar_simbolo_divisa(monedas_test, 'Libra') == 0

    assert detectar_simbolo_divisa(monedas_test, 'Yen') == '¥'

    
