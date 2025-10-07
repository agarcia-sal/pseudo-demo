def multiply(x: int, y: int) -> int:
    p = x % 10
    q = y % 10
    if p < 0:
        p = -p
    if q < 0:
        q = -q
    return p * q