def decimal_to_binary(number_decimal: int) -> str:
    binary_str: str = bin(number_decimal)
    trimmed_binary: str = binary_str[2:]
    prefix_suffix: str = "db"
    result_str: str = prefix_suffix + trimmed_binary + prefix_suffix
    return result_str