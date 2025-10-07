def is_equal_to_sum_even(number_x: int) -> bool:
    if number_x % 2 == 0:
        if number_x >= 8:
            return True
        else:
            return False
    else:
        return False