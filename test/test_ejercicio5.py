
import pytest
from src.ejercicio5 import detectar_y_sumar_creditos

creditos = {'Matemáticas': 6, 'Física': 4, 'Química': 5}


def test_detectar_y_sumar_creditos(capsys):
    assert detectar_y_sumar_creditos(creditos, 0) == 15

    captured = capsys.readouterr()
    assert 'Matemáticas tiene 4 créditos.\nFísica tiene 3 créditos.\nQuímica tiene 2 créditos.\n' == captured.out



