from typing import Union

def decimal_to_binary(decimal: Union[int, float]) -> str:
    """
    Convert an integer decimal number to its binary string representation enclosed within 'db' markers.

    Args:
        decimal (Union[int, float]): The decimal number to convert. Must be an integer value.

    Returns:
        str: A string in the format 'db<binary_string>db'.

    Raises:
        ValueError: If the input is not an integer or is negative.
    """
    if not isinstance(decimal, int) or decimal < 0:
        raise ValueError("Input must be a non-negative integer.")
    binary_string: str = bin(decimal)[2:]  # remove '0b' prefix
    return f"db{binary_string}db"