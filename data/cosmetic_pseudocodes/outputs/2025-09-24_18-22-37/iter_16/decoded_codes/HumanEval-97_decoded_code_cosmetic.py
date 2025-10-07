def multiply(x: int, y: int) -> int:
    p: int = x % 10
    q: int = y % 10
    if p < 0:
        p = -p
    if q < 0:
        q = -q
    return p * q