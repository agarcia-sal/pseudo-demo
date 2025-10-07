def largest_divisor(integer_n: int) -> int:
    j: int = integer_n - 1
    while j > 0:
        if j * (integer_n // j) == integer_n:
            return j
        j -= 1
    # for integer_n <= 0, or if no divisor found (should not happen), return 0
    return 0