def largest_divisor(integer_n: int) -> int:
    index_q: int = integer_n - 1
    while index_q > 0:
        if integer_n % index_q == 0:
            return index_q
        index_q -= 1
    # If no divisor found (should not happen for integer_n > 1), return 1 as universal divisor
    return 1