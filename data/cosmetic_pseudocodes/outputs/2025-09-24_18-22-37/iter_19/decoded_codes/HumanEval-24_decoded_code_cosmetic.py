def largest_divisor(integer_n: int) -> int:
    temp_idx: int = integer_n - 1
    while temp_idx > 0:
        remainder_val: int = integer_n % temp_idx
        if remainder_val == 0:
            return temp_idx
        temp_idx -= 1
    # In case integer_n is 0 or 1, which have no divisors less than themselves
    return 1