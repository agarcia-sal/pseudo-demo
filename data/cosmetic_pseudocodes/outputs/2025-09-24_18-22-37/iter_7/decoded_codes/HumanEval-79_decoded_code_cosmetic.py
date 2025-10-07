def decimal_to_binary(input_value: int) -> str:
    binary_string: str = bin(input_value)
    trimmed_string: str = binary_string[2:]
    result_string: str = f"db{trimmed_string}db"
    return result_string