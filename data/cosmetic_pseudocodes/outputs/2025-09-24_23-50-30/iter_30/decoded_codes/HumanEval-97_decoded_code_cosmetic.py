def multiply(x1: int, y2: int) -> int:
    p = x1 % 10
    q = y2 % 10
    r = p if p >= 0 else -p
    s = q if q >= 0 else -q
    return s * r