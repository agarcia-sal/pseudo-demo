def largest_divisor(integer_n: int) -> int:
    integer_i: int = integer_n - 1
    while integer_i > 0:
        if integer_n % integer_i == 0:
            return integer_i
        integer_i -= 1
    # If no divisor found (only for integer_n <= 0), return 0 as a fallback
    return 0