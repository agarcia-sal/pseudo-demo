def decimal_to_binary(decimal_number: int) -> str:
    binary_str: str = bin(decimal_number)
    trimmed_bin: str = binary_str[2:]
    return f"db{trimmed_bin}db"