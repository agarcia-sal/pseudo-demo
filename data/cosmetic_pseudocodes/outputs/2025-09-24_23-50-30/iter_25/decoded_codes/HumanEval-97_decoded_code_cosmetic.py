def multiply(number_x: int, number_y: int) -> int:
    remainder_x: int = number_x % 10
    remainder_y: int = number_y % 10
    abs_x: int = -remainder_x if remainder_x < 0 else remainder_x
    abs_y: int = -remainder_y if remainder_y < 0 else remainder_y
    return abs_x * abs_y