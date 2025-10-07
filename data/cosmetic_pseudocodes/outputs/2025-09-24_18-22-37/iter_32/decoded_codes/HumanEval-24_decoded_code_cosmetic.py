def largest_divisor(integer_n: int) -> int | None:
    temp_var = integer_n - 1
    while temp_var > 0:
        if integer_n % temp_var == 0:
            return temp_var
        temp_var -= 1
    return None  # In case integer_n <= 0, no divisor found