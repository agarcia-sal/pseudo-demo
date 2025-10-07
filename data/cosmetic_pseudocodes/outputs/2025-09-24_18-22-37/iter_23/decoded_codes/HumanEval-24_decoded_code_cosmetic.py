def largest_divisor(integer_n: int) -> int | None:
    counter_m: int = integer_n - 1
    while counter_m > 0:
        remainder_r: int = integer_n % counter_m
        if remainder_r == 0:
            return counter_m
        counter_m -= 1
    return None  # no divisor found other than 0 which is invalid