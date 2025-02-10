import pytest
import math

from trig import *
from x import X

@pytest.mark.parametrize(
    "x, x_0, res",
    [
        (X(), 0, 1),
        (X(), math.pi / 3, 1 / 2),
        (X(), math.pi / 2, 0),
        (X(), math.pi * 3 / 4, -math.sqrt(2) / 2),
        (X(), math.pi, -1),
        (X(), math.pi * 7 / 6, -math.sqrt(3) / 2),
        (X(), math.pi * 1.5, 0),
    ]
)
def test_sin(x, x_0, res):
    assert Sin(x).df(x_0) == pytest.approx(res)


@pytest.mark.parametrize(
    "x, x_0, res",
    [
        (X(), 0, 0),
        (X(), math.pi / 3, -math.sqrt(3) / 2),
        (X(), math.pi / 2, -1),
        (X(), math.pi * 3 / 4, -math.sqrt(2) / 2),
        (X(), math.pi, 0),
        (X(), math.pi * 7 / 6, 1 / 2),
        (X(), math.pi * 1.5, 1),
    ]
)
def test_cos(x, x_0, res):
    assert Cos(x).df(x_0) == pytest.approx(res)

def tan_derivative(x):
    return 1 / (math.cos(x) ** 2)

@pytest.mark.parametrize(
    "x, x_0, res",
    [
        (X(), 0, tan_derivative(0)),
        (X(), math.pi / 3, tan_derivative(math.pi / 3)),
        (X(), math.pi / 2, tan_derivative(math.pi / 2)),
        (X(), math.pi * 3 / 4, tan_derivative(math.pi * 3 / 4)),
        (X(), math.pi, tan_derivative(math.pi)),
        (X(), math.pi * 7 / 6, tan_derivative(math.pi * 7 / 6)),
        (X(), math.pi * 1.5, tan_derivative(math.pi * 1.5)),
    ]
)
def test_tan(x, x_0, res):
    assert Tan(x).df(x_0) == pytest.approx(res)

def cotan_derivative(x):
    return -1 / (math.sin(x) ** 2)

@pytest.mark.parametrize(
    "x, x_0, res",
    [
        (X(), 0.00001, cotan_derivative(0.00001)),
        (X(), math.pi / 3, cotan_derivative(math.pi / 3)),
        (X(), math.pi / 2, cotan_derivative(math.pi / 2)),
        (X(), math.pi * 3 / 4, cotan_derivative(math.pi * 3 / 4)),
        (X(), math.pi, cotan_derivative(math.pi)),
        (X(), math.pi * 7 / 6, cotan_derivative(math.pi * 7 / 6)),
        (X(), math.pi * 1.5, cotan_derivative(math.pi * 1.5)),
    ]
)
def test_cotan(x, x_0, res):
    assert Cotan(x).df(x_0) == pytest.approx(res)