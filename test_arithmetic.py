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
        (X(), 1, 4, 1),
        (1, X(), 4, 1),
    ]
)
def test_addition(x, y, x_0, res):
    assert (x + y).df(x_0) == pytest.approx(res)

@pytest.mark.parametrize(
    "x, y, x_0, res",
    [
        #(Cos(X()), Sin(X()), 0, -1),
        #(Cos(X()), Sin(math.pi * 0.5 + X()), math.pi * -0.5, 0),
        #(Cos(X()), Sin(math.pi * 1.5 + X()), math.pi * 1.5, 2),
        #(Sin(X()), Cos(X()), math.pi * 0.5, 1),
        (Sin(X() + math.pi), Cos(X() + math.pi * 0.5), 0, 0),
        #(X(), X(), 0, 0),
        #(Sin(X()), X(), 0, 0),
        #(X(), 1, 4, 1),
        #(1, X(), 4, -1),
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
        (X(), Sin(X()), math.pi / 3, (6 * math.sqrt(3) - 2 * math.pi) / 9),
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
        #(Sin(X()), Cos(X()), math.pi * 0.5), TODO: maybe add a warning when divisor approaches zero about possibility of errors due to machine representation
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
        (X(), -2, 3, -2 / 27),
        (X(), math.e, math.pi, math.e * math.pi ** (math.e - 1)),
        (Cos(X()), 2, math.pi / 4, math.sqrt(2)),
        (X(), 0, 434, 0),
    ]
)
def test_power(x, y, x_0, res):
    assert (x ** y).df(x_0) == pytest.approx(res)

@pytest.mark.parametrize(
    "x, y, x_0, res",
    [
        (0, Sin(X()), 3, 0),
        (1, Sin(X()), 3, 0),
        (2, 2 * X(), 3, 11.09035488895912),
        (X(), Cos(X()), math.e, -0.299838984544407),
    ]
)
def test_exponential(x, y, x_0, res):
    assert (x ** y).df(x_0) == pytest.approx(res)