""" Test cases for the division function."""
import pytest
from app.division import divide

def test_divide():
    """Test the divide function."""
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(-10, 2) == -5

def test_divide_zero_exception():
    """Test that division by zero raises a ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
