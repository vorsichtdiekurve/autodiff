import pytest
import math

from logn import Logn
from trig import Sin, Cos
from x import X

@pytest.mark.parametrize(
    "x, x_0, res",
    [
        (Sin(Cos(Sin(Cos(X())))), 0.3, 0.0963065647258788),
        (Cos(Sin(Cos(Cos(X())))), math.e, 0.144475893363656),
        (Sin(math.pi * X()), 0, math.pi),
        (Logn(Sin(X())), math.e, 1/math.tan(math.e)),
    ]
)
def test_chain_rule(x, x_0, res):
    assert x.df(x_0) == pytest.approx(res)