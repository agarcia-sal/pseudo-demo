def is_equal_to_sum_even(check_value: int) -> bool:
    if check_value < 8:
        return False
    else:
        return check_value % 2 == 0