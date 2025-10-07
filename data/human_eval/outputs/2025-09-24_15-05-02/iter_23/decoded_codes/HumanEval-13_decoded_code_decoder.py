from typing import Union


def greatest_common_divisor(a: int, b: int) -> int:
    """
    Compute the greatest common divisor (GCD) of two integers using
    the Euclidean algorithm.
    """
    # Ensure inputs are integers
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Inputs must be integers")
    # Handle negative inputs by converting to absolute values
    a, b = abs(a), abs(b)
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a