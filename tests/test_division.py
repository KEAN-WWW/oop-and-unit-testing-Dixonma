""" Test cases for the division function."""
import pytest
from app.division import divide

def test_divide():
    """Test the divide function."""
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(-10, 2) == -5

    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)
