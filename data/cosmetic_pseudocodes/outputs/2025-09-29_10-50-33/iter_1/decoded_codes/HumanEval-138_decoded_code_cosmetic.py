def is_equal_to_sum_even(integer_n: int) -> bool:
    if integer_n % 2 != 0:
        return False
    elif integer_n < 8:
        return False
    else:
        return True