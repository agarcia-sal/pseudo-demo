def greatest_common_divisor(num_x: int, num_y: int) -> int:
    while num_y != 0:
        placeholder = num_y
        num_y = num_x % num_y
        num_x = placeholder
    return num_x