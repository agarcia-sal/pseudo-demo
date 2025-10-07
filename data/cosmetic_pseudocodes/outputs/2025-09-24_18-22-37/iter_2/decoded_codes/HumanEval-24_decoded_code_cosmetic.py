def largest_divisor(integer_n: int) -> int:
    candidate = integer_n - 1
    while candidate > 0:
        if integer_n % candidate == 0:
            return candidate
        candidate -= 1
    # For integer_n <= 0, no positive divisor other than possibly integer_n itself; handle gracefully
    return 0