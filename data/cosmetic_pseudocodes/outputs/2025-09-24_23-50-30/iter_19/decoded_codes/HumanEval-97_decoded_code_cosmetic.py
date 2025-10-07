from math import floor

def multiply(x: int, y: int) -> int:
    a = x - floor(x / 10) * 10
    b = y - floor(y / 10) * 10
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    return a * b