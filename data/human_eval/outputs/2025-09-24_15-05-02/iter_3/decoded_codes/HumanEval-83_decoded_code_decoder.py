def starts_one_ends(n: int) -> int:
    """
    Returns the count of n-digit numbers that start with 1 and end with 1.

    Args:
        n (int): Number of digits

    Returns:
        int: The count of such numbers
    """
    if n == 1:
        return 1
    return 18 * (10 ** (n - 2))