import math

import pytest

from x import X
from logn import Logn

@pytest.mark.parametrize(
    "x, x_0, res",
    [
        (X(), 4, 1 / 4),
        (3 * X() ** 2, 5, 2 / 5),
        (math.e ** X(), math.pi, 1)
    ]
)
def test_log(x, x_0, res):
    assert Logn(x).df(x_0) == pytest.approx(res)