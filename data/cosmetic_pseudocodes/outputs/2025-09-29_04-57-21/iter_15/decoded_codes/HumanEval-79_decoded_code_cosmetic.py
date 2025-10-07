def decimal_to_binary(decimal_number: int) -> str:
    binary_string = bin(decimal_number)
    trimmed_binary = binary_string[1:]
    return f"db{trimmed_binary}db"