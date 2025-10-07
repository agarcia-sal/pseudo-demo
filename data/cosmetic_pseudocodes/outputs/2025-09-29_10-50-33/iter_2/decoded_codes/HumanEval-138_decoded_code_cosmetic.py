def is_equal_to_sum_even(number_value: int) -> bool:
    if number_value % 2 == 0:
        return number_value >= 8
    return False