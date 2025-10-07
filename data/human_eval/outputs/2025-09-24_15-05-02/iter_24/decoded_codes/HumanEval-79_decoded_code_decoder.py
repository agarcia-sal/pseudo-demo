def decimal_to_binary(decimal: int) -> str:
    binary_string: str = bin(decimal)[2:]
    return f"db{binary_string}db"