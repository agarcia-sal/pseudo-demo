def greatest_common_divisor(a: int, b: int) -> int:
    while b != 0:
        temp = a
        a = b
        b = temp % b
    return a