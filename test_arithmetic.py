import math

import pytest

from x import X
from sin import Sin
from cos import Cos
from base import Base

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
        (Cos(X()), Sin(math.pi * 0.5 + X()), math.pi * -0.5, 1),
        (Cos(X()), Sin(math.pi * 1.5 + X()), math.pi * 1.5, 2),
        (Sin(X()), Cos(X()), math.pi * 0.5, 1),
        (Sin(X() + math.pi), Cos(X() + math.pi * 0.5), 0, 0),
        (X(), X(), 0, 0),
        (Sin(X()), X(), 0, 0),
    ]
)
def test_subtraction(x, y, x_0, res):
    assert (x - y).df(x_0) == pytest.approx(res)