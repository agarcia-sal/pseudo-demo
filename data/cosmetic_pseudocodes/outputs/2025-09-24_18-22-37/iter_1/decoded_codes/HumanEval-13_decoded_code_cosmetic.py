def greatest_common_divisor(x: int, y: int) -> int:
    while y != 0:
        temp = y
        y = x % y
        x = temp
    return x