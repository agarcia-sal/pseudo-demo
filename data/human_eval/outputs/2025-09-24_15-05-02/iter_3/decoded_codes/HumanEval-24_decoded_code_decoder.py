def largest_divisor(n: int) -> int:
    """
    Returns the largest divisor of n less than n itself.
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i