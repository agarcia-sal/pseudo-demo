def greatest_common_divisor(a: int, b: int) -> int:
    while b != 0:
        temporary = b
        b = a % b
        a = temporary
    return a