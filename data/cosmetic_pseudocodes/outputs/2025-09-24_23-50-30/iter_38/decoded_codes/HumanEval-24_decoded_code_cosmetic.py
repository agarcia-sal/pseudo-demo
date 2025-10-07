def largest_divisor(alpha: int) -> int:
    beta = alpha - 1
    while beta > 0:
        if alpha % beta == 0:
            return beta
        beta -= 1
    return 0  # No divisor found other than 0 if alpha <= 1