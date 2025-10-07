def is_simple_power(x: int, n: int) -> bool:
    """
    Check if x is a power of n, i.e., if there exists an integer k >= 0 such that n^k == x.

    Args:
        x (int): The number to check.
        n (int): The base number.

    Returns:
        bool: True if x is a power of n, False otherwise.
    """

    # Special case: if n is 1, x must also be 1 to be a power of n
    if n == 1:
        return x == 1

    power = 1
    # Multiply power by n until it reaches or exceeds x
    while power < x:
        power *= n

    # Check if power exactly equals x
    return power == x