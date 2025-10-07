def multiply(num_x: int, num_y: int) -> int:
    remainder_x = num_x % 10
    if remainder_x < 0:
        remainder_x = -remainder_x

    remainder_y = num_y % 10
    if remainder_y < 0:
        remainder_y = -remainder_y

    product = remainder_x * remainder_y
    return product