def largest_divisor(integer_n: int) -> int:
    x: int = integer_n - 1
    while x > 0:
        if integer_n % x == 0:
            return x
        x -= 1
    # If no divisor found (which is impossible for integers > 1), return 1 as fallback
    return 1