def largest_divisor(integer_n: int) -> int:
    candidate: int = integer_n - 1
    while candidate > 0:
        if integer_n % candidate == 0:
            return candidate
        candidate -= 1
    # If integer_n <= 1, no divisors less than integer_n exist, return 0 as fallback
    return 0