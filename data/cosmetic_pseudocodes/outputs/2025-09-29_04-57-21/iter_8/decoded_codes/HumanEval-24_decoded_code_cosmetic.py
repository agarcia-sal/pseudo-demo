def largest_divisor(integer_n: int) -> int:
    candidate = integer_n - 1
    while candidate > 0:
        if integer_n % candidate == 0:
            return candidate
        candidate -= 1
    # If integer_n is 0 or 1, no divisor less than integer_n exists, return 0 as fallback
    return 0