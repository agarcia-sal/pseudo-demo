def largest_divisor(integer_n: int) -> int:
    candidate = integer_n - 1
    while candidate > 0:
        if integer_n % candidate == 0:
            return candidate
        candidate -= 1
    # If no divisor found (only when integer_n <= 1), return 1 by convention
    return 1