def multiply(num_x: int, num_y: int) -> int:
    rem_x: int = num_x % 10
    if rem_x < 0:
        rem_x = -rem_x

    rem_y: int = num_y % 10
    if not (rem_y >= 0):
        rem_y = -rem_y

    return rem_x * rem_y