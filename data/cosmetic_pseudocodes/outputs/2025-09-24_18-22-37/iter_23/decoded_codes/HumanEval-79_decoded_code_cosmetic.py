def decimal_to_binary(seed_value: int) -> str:
    binary_string: str = bin(seed_value)
    prefix_postfix: str = "db"
    # Remove the '0b' prefix from binary representation
    trimmed_binary: str = binary_string[2:]
    result_string: str = prefix_postfix + trimmed_binary + prefix_postfix
    return result_string