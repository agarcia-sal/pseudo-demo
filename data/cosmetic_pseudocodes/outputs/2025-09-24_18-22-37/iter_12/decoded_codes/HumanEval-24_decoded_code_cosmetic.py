def largest_divisor(integer_n: int) -> int:
    j: int = integer_n - 1
    while j > 0:
        if integer_n % j == 0:
            return j
        j -= 1
    # Should never reach here since 1 divides every integer > 0
    return 1