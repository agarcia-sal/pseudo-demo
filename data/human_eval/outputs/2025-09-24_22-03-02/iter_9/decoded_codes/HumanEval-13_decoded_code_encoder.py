def greatest_common_divisor(a: int, b: int) -> int:
    while b != 0:
        temporary_value = b
        b = a % b
        a = temporary_value
    return a