def largest_divisor(integer_n: int) -> int:
    integer_p: int = integer_n - 1
    while integer_p > 0:
        remainder_check: int = integer_n % integer_p
        if remainder_check == 0:
            return integer_p
        integer_p -= 1
    # theoretically unreachable for integer_n > 1, but handle edge cases
    return 1