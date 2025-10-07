def multiply(x1: int, x2: int) -> int:
    r1: int = x1 % 10
    r2: int = x2 % 10
    s1: int = -r1 if r1 < 0 else r1
    s2: int = -r2 if r2 < 0 else r2
    return s1 * s2