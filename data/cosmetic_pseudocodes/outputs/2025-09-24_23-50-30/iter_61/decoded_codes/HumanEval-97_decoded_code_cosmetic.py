def multiply(x1: int, y2: int) -> int:
    # The switch with immediate exit is effectively a no-op
    # Return product of absolute values of last digits of x1 and y2
    return abs(x1 % 10) * abs(y2 % 10)