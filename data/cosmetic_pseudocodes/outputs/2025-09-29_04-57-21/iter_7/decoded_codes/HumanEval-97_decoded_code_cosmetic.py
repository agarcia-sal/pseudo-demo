def multiply(num_x: int, num_y: int) -> int:
    rem_x = num_x % 10
    rem_y = num_y % 10
    abs_x = -rem_x if rem_x < 0 else rem_x
    abs_y = -rem_y if rem_y < 0 else rem_y
    return abs_x * abs_y