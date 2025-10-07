def decimal_to_binary(value: int) -> str:
    binary_string = bin(value)
    trimmed_binary = binary_string[2:]
    return f"db{trimmed_binary}db"