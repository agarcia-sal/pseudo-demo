def largest_divisor(integer_n: int) -> int:
    candidate = integer_n - 1
    while candidate > 0:
        if integer_n % candidate == 0:
            return candidate
        candidate -= 1
    # In case integer_n is 1 or 0, no divisor less than integer_n exists, return 0
    return 0