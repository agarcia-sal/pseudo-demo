def decimal_to_binary(input_value: int) -> str:
    prefix_suffix = "db"
    binary_form = bin(input_value)
    trimmed_binary = binary_form[2:]
    assembled_string = prefix_suffix + trimmed_binary + prefix_suffix
    return assembled_string