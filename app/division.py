def divide(val1: int, val2: int) -> float:
    if val2 == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return val1 / val2
