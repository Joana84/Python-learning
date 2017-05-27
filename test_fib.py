import fib
import pytest

def test_mul():
    result = fib.mul(4, 3)
    assert result == 12

@pytest.mark.parametrize('a, b, expected_output',
                        [
                        (1, 1, 0),
                        (2, 9, -7 ),
                        (-2, 2, -4),
                        (-2, -2, 0)
                        ]
)
def test_sub(a, b, expected_output):
    result = fib.sub(a, b)
    assert result == expected_output
