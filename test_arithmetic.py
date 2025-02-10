import math

import pytest

from x import X
from sin import Sin
from cos import Cos

@pytest.mark.parametrize(
    "x, y, x_0, res",
    [
        (Cos(X()), Sin(X()), 0, 1),
        (Cos(X()), Sin(math.pi * 0.5 + X()), math.pi * -0.5, 2),
        (Cos(X()), Sin(math.pi * 1.5 + X()), math.pi * 1.5, 0),
        (Sin(X()), Cos(X()), math.pi * 0.5, -1),
        (Sin(X() + math.pi), Cos(X() + math.pi * 0.5), 0, -2),
        (X(), X(), 0, 2),
        (Sin(X()), X(), 0, 2),
    ]
)
def test_addition(x, y, x_0, res):
    assert (x + y).df(x_0) == pytest.approx(res)

@pytest.mark.parametrize(
    "x, y, x_0, res",
    [
        (Cos(X()), Sin(X()), 0, -1),
        (Cos(X()), Sin(math.pi * 0.5 + X()), math.pi * -0.5, 0),
        (Cos(X()), Sin(math.pi * 1.5 + X()), math.pi * 1.5, 2),
        (Sin(X()), Cos(X()), math.pi * 0.5, 1),
        (Sin(X() + math.pi), Cos(X() + math.pi * 0.5), 0, 0),
        (X(), X(), 0, 0),
        (Sin(X()), X(), 0, 0),
    ]
)
def test_subtraction(x, y, x_0, res):
    assert (x - y).df(x_0) == pytest.approx(res)

@pytest.mark.parametrize(
    "x, y, x_0, res",
    [
        (Cos(X()), 5, 0, 0),
        (X(), Sin(X()), math.pi, -math.pi),
        (2, Cos(X()), math.pi * 1.5 , 2),
    ]
)
def test_multiplication(x, y, x_0, res):
    assert (x * y).df(x_0) == pytest.approx(res)

@pytest.mark.parametrize(
    "x, y, x_0, res",
    [
        (Cos(X()), 5, math.pi * 0.5, -0.2),
        (X(), Sin(X()), math.pi / 3, 2 * (1 - math.pi * math.sqrt(3))),
        (2, Cos(X()), math.pi / 4 , 2 * math.sqrt(2)),
    ]
)
def test_division(x, y, x_0, res):
    assert (x / y).df(x_0) == pytest.approx(res)

@pytest.mark.parametrize(
    "x, y, x_0",
    [
        (X(), 0, 0),
        (Cos(X()), Sin(X()), 0),
        (Sin(X()), Cos(X()), math.pi * 0.5),
    ]
)
def test_division_by_zero_raises_zero_division_error(x, y, x_0):
    with pytest.raises(ZeroDivisionError):
        (x / y).df(x_0)

@pytest.mark.parametrize(
    "x, y, x_0, res",
    [
        (X(), 2, 3, 6),
        (X(), 9, 2, 9 * 256),
        (X(), -2, 3, -13.5),
        (X(), math.e, math.pi, math.e * math.pi ** (math.e - 1)),
        (Cos(X()), 2, math.pi / 4, -1)
    ]
)
def test_power(x, y, x_0, res):
    assert (x ** y).df(x_0) == pytest.approx(res)