def largest_divisor(integer_n: int) -> int:
    j: int = integer_n - 1
    while j > 0:
        if integer_n % j == 0:
            return j
        j -= 1
    # if no divisor is found (which can only happen if integer_n <= 1), return 1
    return 1