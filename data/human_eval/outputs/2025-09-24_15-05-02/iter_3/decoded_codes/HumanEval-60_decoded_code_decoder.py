def sum_to_n(n: int) -> int:
    """
    Returns the sum of all integers from 0 to n inclusive.
    Uses the arithmetic series formula for optimal performance.
    """
    if n < 0:
        return 0  # Assuming sum for negative n is 0, adjust if needed
    return n * (n + 1) // 2