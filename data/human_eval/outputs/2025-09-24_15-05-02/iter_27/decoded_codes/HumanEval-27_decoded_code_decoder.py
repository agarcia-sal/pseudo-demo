def flip_case(string: str) -> str:
    if not isinstance(string, str):
        raise ValueError("Input must be a string")
    return string.swapcase()