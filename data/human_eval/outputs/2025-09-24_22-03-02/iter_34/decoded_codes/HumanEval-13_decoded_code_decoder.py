def greatest_common_divisor(a: int, b: int) -> int:
    while b != 0:
        temp = b
        remainder = a % b
        a = temp
        b = remainder
    return a