def decimal_to_binary(decimal_number: int) -> str:
    binary_str = bin(decimal_number)
    trimmed_binary = binary_str[2:]
    return f"db{trimmed_binary}db"