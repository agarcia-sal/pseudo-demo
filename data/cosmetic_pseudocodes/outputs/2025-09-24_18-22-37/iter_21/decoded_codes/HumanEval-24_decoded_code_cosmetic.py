def largest_divisor(number_p: int) -> int:
    integer_q: int = number_p - 1
    while integer_q > 0:
        remainder_s: int = number_p % integer_q
        if remainder_s == 0:
            return integer_q
        integer_q -= 1
    # If no divisor found (shouldn't happen for integers > 1), return 1 as a fallback
    return 1