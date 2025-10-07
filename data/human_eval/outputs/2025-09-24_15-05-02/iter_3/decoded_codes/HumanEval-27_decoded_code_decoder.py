def flip_case(string: str) -> str:
    """
    Returns a new string where each lowercase character is converted to uppercase,
    and each uppercase character is converted to lowercase.
    Non-alphabetic characters remain unchanged.
    """
    return string.swapcase()