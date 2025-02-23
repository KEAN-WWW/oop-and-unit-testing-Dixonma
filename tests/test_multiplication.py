""" Test cases for the multiplication function."""

from app.multiplication import multiply

def test_multiply():
    """Test the multiply function."""
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10
    assert multiply(0, 100) == 0
