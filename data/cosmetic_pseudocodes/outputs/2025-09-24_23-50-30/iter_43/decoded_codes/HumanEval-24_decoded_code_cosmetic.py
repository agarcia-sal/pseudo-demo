def largest_divisor(integer_n: int) -> int:
    integer_j: int = integer_n - 1
    while integer_j > 0:
        if integer_n % integer_j == 0:
            return integer_j
        integer_j -= 1
    # In case no divisor found (should not happen for integer_n > 1)
    return 1