import pytest
from app.subtraction import subtract

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(10, 20) == -10
    assert subtract(0, 0) == 0
