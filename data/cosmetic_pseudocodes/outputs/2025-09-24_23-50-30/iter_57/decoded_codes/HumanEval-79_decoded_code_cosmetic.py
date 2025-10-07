def decimal_to_binary(num_decimal: int) -> str:
    binary_str: str = bin(num_decimal)
    partial_str: str = binary_str[2:]
    result_str: str = "db" + partial_str + "db"
    return result_str