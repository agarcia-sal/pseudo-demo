def multiply(x1: int, y2: int) -> int:
    r3 = x1 % 10
    s4 = y2 % 10
    if r3 < 0:
        r3 = -r3
    if s4 < 0:
        s4 = -s4
    return r3 * s4