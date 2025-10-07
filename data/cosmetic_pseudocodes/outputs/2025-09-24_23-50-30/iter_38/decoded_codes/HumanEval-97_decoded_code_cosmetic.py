def multiply(alpha: int, beta: int) -> int:
    a = alpha % 10
    if a < 0:
        a = -a
    b = beta % 10
    if b < 0:
        b = -b
    return a * b