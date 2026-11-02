import pytest
from app import calculate_fine

@pytest.mark.parametrize("days, expected", [
    (0, 0),
    (2, 10),
    (5, 25),
    (1, 5),
])
def test_valid_fine(days, expected):
    assert calculate_fine(days) == expected

def test_negative_days():
    with pytest.raises(ValueError):
        calculate_fine(-1)

def test_invalid_input():
    with pytest.raises(ValueError):
        calculate_fine("abc")

def test_boundary():
    assert calculate_fine(1) == 5
