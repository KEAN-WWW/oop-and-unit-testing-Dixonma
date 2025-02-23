""" Test cases for the subtraction function."""
import pytest
from app.subtraction import subtract


def test_subtract():

    """Test the subtract function."""
    assert subtract(5, 3) == 2
    assert subtract(10, 20) == -10
    assert subtract(0, 0) == 0

    with pytest.raises(TypeError):
        subtract(10, "5")
