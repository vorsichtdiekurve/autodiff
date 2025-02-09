import pytest
import math

from sin import Sin
from cos import Cos
from x import X

@pytest.mark.parametrize(
    "x, x_0, res",
    [
        (Sin(Cos(Sin(Cos(X())))), 0.3, 0.0963065647258788),
        (Cos(Sin(Cos(Cos(X())))), math.e, 0.144475893363656),
    ]
)
def test_chain_rule(x, x_0, res):
    assert x.df(x_0) == pytest.approx(res)