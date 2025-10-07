def greatest_common_divisor(x: int, y: int) -> int:
    while True:
        if y == 0:
            break
        z = y
        y = x - (x // y) * y  # remainder of x divided by y
        x = z
    return x