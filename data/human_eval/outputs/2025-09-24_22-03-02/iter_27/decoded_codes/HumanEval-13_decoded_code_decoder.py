def greatest_common_divisor(a: int, b: int) -> int:
    while b != 0:
        temp: int = b
        b: int = a % b
        a: int = temp
    return a