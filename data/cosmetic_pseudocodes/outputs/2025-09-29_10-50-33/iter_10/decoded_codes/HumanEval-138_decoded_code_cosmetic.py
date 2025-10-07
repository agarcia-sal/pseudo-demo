def is_equal_to_sum_even(integer_n: int) -> bool:
    if not (integer_n % 2 != 0):
        if not (integer_n < 8):
            return True
        return False
    return False