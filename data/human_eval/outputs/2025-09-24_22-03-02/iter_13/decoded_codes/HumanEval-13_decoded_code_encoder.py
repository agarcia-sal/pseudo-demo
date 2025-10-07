def greatest_common_divisor(a: int, b: int) -> int:
    while b != 0:
        temporary_a = b
        temporary_b = a % b
        a = temporary_a
        b = temporary_b
    return a