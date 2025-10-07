def greatest_common_divisor(a: int, b: int) -> int:
    while b != 0:
        temp_a = a
        a = b
        b = temp_a % b
    return a