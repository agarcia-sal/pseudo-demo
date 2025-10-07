def largest_divisor(integer_n: int) -> int:
    candidate: int = integer_n - 1
    while candidate > 0:
        if integer_n % candidate == 0:
            return candidate
        candidate -= 1
    # If no divisor found (which can't happen for integer_n > 1), return 1
    return 1