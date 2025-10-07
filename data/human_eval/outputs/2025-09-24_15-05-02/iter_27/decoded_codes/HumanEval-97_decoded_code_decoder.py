from typing import Union

def multiply(a: Union[int, float], b: Union[int, float]) -> int:
    """
    Returns the product of the absolute values of the last digits of a and b.

    The last digit is taken by modulo 10 of the integer part of each input.
    """
    try:
        last_digit_a: int = abs(int(a) % 10)
        last_digit_b: int = abs(int(b) % 10)
    except (ValueError, TypeError) as e:
        raise ValueError("Inputs must be numeric values.") from e

    return last_digit_a * last_digit_b