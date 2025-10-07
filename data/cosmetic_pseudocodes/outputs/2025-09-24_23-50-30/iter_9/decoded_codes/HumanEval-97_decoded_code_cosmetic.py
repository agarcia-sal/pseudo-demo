def multiply(x: int, y: int) -> int:
    p = x - (x // 10) * 10
    q = y - (y // 10) * 10
    if p < 0:
        p = -p
    if q < 0:
        q = -q
    return p * q