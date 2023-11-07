
from src.ejercicio1 import detectar_simbolo_divisa, monedas

def test_detectar_simbolo_divisa():
    assert detectar_simbolo_divisa(monedas , "Euro") == "€"