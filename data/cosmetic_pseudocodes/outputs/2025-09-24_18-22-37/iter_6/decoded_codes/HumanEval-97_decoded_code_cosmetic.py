def multiply(num_x: int, num_y: int) -> int:
    rem_x: int = num_x % 10
    rem_y: int = num_y % 10

    abs_rem_x: int = -rem_x if rem_x < 0 else rem_x
    abs_rem_y: int = -rem_y if rem_y < 0 else rem_y

    result: int = abs_rem_x * abs_rem_y
    return result