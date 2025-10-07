def greatest_common_divisor(a: int, b: int) -> int:
    while b != 0:
        temp_a = a
        temp_b = b
        a = temp_b
        b = temp_a % temp_b
    return a