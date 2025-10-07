def largest_divisor(integer_n: int) -> int:
    alpha = integer_n - 1
    while alpha > 0:
        beta = integer_n % alpha
        if beta == 0:
            return alpha
        alpha -= 1
    # If no divisor found (which doesn't happen for integer_n > 1), return 1 as fallback
    return 1