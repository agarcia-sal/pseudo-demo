def largest_divisor(integer_n: int) -> int:
    divisor_candidate = integer_n - 1
    while divisor_candidate > 0:
        if integer_n % divisor_candidate == 0:
            return divisor_candidate
        divisor_candidate -= 1
    # If no divisor found (for n=1), return 0 as no positive divisor less than n exists
    return 0