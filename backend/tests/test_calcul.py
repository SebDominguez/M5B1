from modules.calcul import calcul


def test_calcul_positive():
    assert calcul(5) == 25


def test_calcul_zero():
    assert calcul(0) == 0


def test_calcul_negative():
    assert calcul(-4) == 16
