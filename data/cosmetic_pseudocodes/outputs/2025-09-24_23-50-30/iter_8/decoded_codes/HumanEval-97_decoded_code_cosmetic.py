def multiply(x: int, y: int) -> int:
    p = abs(x) - (abs(x) // 10) * 10
    q = abs(y) - (abs(y) // 10) * 10
    return p * q