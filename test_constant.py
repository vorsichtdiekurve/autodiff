import math

import pytest

from logn import Logn
from trig import Sin, Cos

@pytest.mark.parametrize(
    "x, x_0",
    [
        (Cos(0), 0), (Cos(-1), 1), (Cos(1), -1),
        (Sin(0), 0), (Sin(-1), 1), (Sin(1), -1),
        (Logn(math.e), 0)
    ]
)
def test_derivative_of_constant_returns_zero(x, x_0):
    assert x.df(x_0) == 0