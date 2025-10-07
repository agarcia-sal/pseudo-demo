def largest_divisor(integer_n: int) -> int:
    j: int = integer_n - 1
    while j > 0:
        if integer_n % j == 0:
            return j
        j -= 1
    # No divisor found other than 1 (if integer_n > 1), return 1 as fallback
    return 1