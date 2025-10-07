def greatest_common_divisor(x: int, y: int) -> int:
    if y == 0:
        return x
    else:
        return greatest_common_divisor(y, x % y)