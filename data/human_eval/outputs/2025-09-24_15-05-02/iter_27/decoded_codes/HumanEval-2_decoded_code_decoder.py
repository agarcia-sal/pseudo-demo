from typing import Union

def truncate_number(number: Union[int, float]) -> float:
    """
    Returns the fractional part of the input number.
    Raises ValueError if input is not a number.
    """
    if not isinstance(number, (int, float)):
        raise ValueError("Input must be an integer or float.")
    return number % 1.0