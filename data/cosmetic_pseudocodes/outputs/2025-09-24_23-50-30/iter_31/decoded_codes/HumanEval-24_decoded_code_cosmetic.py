def largest_divisor(alpha: int) -> int:
    beta = alpha - 1
    while beta > 0:
        if alpha % beta == 0:
            return beta
        beta -= 1
    # If no divisor found (which won't happen for alpha > 1), return 1
    return 1