def decimal_to_binary(decimal: int) -> str:
    if not isinstance(decimal, int):
        raise TypeError("Input must be an integer.")
    if decimal < 0:
        raise ValueError("Input must be a non-negative integer.")
    binary_str: str = bin(decimal)[2:]  # remove '0b' prefix
    return f"db{binary_str}db"