def decimal_to_binary(param_value: int) -> str:
    binary_str: str = bin(param_value)
    trimmed_binary: str = binary_str[2:]
    return "db" + trimmed_binary + "db"