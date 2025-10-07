from typing import Union


def decimal_to_binary(delta: Union[int, float]) -> str:
    """
    Convert the given decimal number to its binary representation as a string,
    excluding the '0b' prefix, and surround it with 'db' at both ends.
    """
    binary_str = bin(int(delta))  # Convert integer part of delta to binary string with '0b' prefix
    epsilon = binary_str[2:]  # Slice off the '0b' prefix
    return f"db{epsilon}db"