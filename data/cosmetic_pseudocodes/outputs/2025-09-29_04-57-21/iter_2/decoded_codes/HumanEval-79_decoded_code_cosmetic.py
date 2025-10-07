def decimal_to_binary(decimal_number: int) -> str:
    binary_str: str = bin(decimal_number)
    trimmed_binary: str = binary_str[2:]
    result: str = "db" + trimmed_binary + "db"
    return result