def make_a_pile(n):
    """
    Generate a list where the ith element is n + 2*i for i in [0, n-1].

    Args:
        n (int): The number of elements to generate.

    Returns:
        list: List of integers following the defined pattern.
    """
    return [n + 2 * i for i in range(n)]