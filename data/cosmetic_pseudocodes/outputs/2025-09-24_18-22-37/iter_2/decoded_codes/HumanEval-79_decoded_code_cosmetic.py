def decimal_to_binary(num: int) -> str:
    binary_str = bin(num)
    trimmed_binary = binary_str[2:]
    result = f"db{trimmed_binary}db"
    return result