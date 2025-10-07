def decimal_to_binary(input_value: int) -> str:
    binary_string: str = bin(input_value)
    trimmed_bits: str = binary_string[2:]
    prefix_suffix: str = "db" + trimmed_bits + "db"
    return prefix_suffix