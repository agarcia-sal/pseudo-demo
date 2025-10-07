def monotonic(l):
    """
    Check if the list is monotonic (entirely non-increasing or non-decreasing).

    Args:
        l (list): List of comparable elements.

    Returns:
        bool: True if l is monotonic, False otherwise.
    """
    return l == sorted(l) or l == sorted(l, reverse=True)