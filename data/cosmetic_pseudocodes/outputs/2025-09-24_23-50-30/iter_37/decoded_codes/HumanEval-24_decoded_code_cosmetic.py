def largest_divisor(integer_n: int) -> int:
    lattic: int = integer_n - 1
    while lattic > 0:
        if integer_n % lattic == 0:
            return lattic
        lattic -= 1
    # If no divisor found (should not happen for integer_n > 1), return 1
    return 1