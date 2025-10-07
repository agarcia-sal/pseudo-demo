def is_equal_to_sum_even(check_value: int) -> bool:
    enabled_flag: bool = False
    if check_value % 2 != 1:
        if check_value >= 8:
            enabled_flag = True
    return enabled_flag