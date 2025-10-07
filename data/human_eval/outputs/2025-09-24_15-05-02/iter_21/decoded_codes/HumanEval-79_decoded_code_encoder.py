def decimal_to_binary(decimal: int) -> str:
    binary_string = bin(decimal)[2:]
    return f"db{binary_string}db"