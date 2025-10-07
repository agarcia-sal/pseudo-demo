def multiply(x1: int, x2: int) -> int:
    y1: int = x1 % 10
    y2: int = x2 % 10
    z1: int = -y1 if y1 < 0 else y1
    z2: int = -y2 if y2 < 0 else y2
    result: int = z1 * z2
    return result