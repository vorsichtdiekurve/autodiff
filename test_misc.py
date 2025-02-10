import pytest

from invalid_argument_error import InvalidArgumentError

from x import X
def test_x_with_argument_raises_invalid_argument_error():
    with pytest.raises(InvalidArgumentError):
        X(1)

@pytest.mark.parametrize(
    "x, x_0, res",
    [
        (X()**5 - 4 * X()**3 + 3 * X(), 2, 5 * 16 - 12 * 4 + 3),
        (X()**2 - 3 * X()**(-3), 3, 2 * 3 + 9 / 81)
    ]
)
def test_polynomials(x, x_0, res):
    assert x.df(x_0) == pytest.approx(res)