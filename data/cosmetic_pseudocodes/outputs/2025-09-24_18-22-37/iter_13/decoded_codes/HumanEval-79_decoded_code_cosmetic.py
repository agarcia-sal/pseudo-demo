def decimal_to_binary(input_value: int) -> str:
    prefix = "db"
    binary_string = bin(input_value)
    trimmed_binary = binary_string[2:]
    suffix = "db"
    combined_result = prefix + trimmed_binary + suffix
    return combined_result