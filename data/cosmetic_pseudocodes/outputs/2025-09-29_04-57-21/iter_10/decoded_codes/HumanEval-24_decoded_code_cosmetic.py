def largest_divisor(integer_n: int) -> int:
    candidate = integer_n - 1
    while candidate > 0:
        if integer_n % candidate == 0:
            return candidate
        candidate -= 1
    # Edge case: if no divisor found (e.g., integer_n == 1), return 0 as no divisor less than n
    return 0