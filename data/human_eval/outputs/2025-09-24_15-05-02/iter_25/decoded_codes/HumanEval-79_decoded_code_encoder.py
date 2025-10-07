def decimal_to_binary(decimal: int) -> str:
    binary_string: str = bin(decimal)[2:]  # Convert to binary and remove '0b' prefix
    result: str = f"db{binary_string}db"
    return result