def largest_divisor(integer_n: int) -> int:
    j = integer_n - 1
    while j > 0:
        if integer_n % j == 0:
            return j
        j -= 1
    # In case no divisor found (should not happen for integers > 1), return 1 as fallback
    return 1