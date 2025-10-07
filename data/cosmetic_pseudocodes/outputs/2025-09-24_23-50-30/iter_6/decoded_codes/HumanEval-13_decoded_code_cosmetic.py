def greatest_common_divisor(integer_a: int, integer_b: int) -> int:
    q: int = integer_a
    w: int = integer_b
    while w != 0:
        x: int = w
        w = q - (q // w) * w
        q = x
    return q