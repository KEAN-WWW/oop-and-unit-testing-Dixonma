""" Test cases for the addition function."""
import pytest
from app.addition import add


def test_add():
    """Test the add function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

    with pytest.raises(TypeError):
        add(None, 5)
