def largest_divisor(integer_n: int) -> int:
    candidate: int = integer_n - 1
    while candidate > 0:
        if integer_n % candidate == 0:
            return candidate
        candidate -= 1
    # Optional: handle the case where no divisor found (only for 0 or 1)
    return 1