def is_equal_to_sum_even(value_x: int) -> bool:
    if value_x <= 7:
        return False
    if value_x % 2 != 0:
        return False
    return True