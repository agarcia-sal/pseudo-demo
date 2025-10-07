def decimal_to_binary(input_value: int) -> str:
    prefix_suffix: str = "db"
    binary_str: str = bin(input_value)
    sliced_str: str = binary_str[2:]
    return prefix_suffix + sliced_str + prefix_suffix